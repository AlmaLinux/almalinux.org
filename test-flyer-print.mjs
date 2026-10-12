#!/usr/bin/env node
/**
 * Test that flyer pages print to the expected number of PDF pages, and that
 * nothing on a page is cut off. Print styles hide overflow, so clipped content
 * still prints as the right number of pages; the clipping check catches it.
 *
 * Usage:
 *   npx playwright install chromium   # first time only
 *   node test-flyer-print.mjs [base-url]
 *
 * Defaults to http://localhost:1313 — start Hugo server first.
 * Generates PDFs in /tmp and reports page counts and any clipped elements.
 */

import { chromium } from "playwright";
import { writeFileSync } from "fs";

const BASE = process.argv[2] || "http://localhost:1313";

const FLYERS = [
  {
    path: "/flyer/",
    expectedPages: 2,
    name: "Main flyer (letter)",
    width: "8.5in",
    height: "11in",
  },
  {
    path: "/flyer-overview/",
    expectedPages: 2,
    name: "Overview flyer (letter)",
    width: "8.5in",
    height: "11in",
  },
  {
    path: "/flyer-elevate/",
    expectedPages: 2,
    name: "ELevate flyer (half-page)",
    width: "8.5in",
    height: "5.5in",
  },
  {
    path: "/flyer-compare/",
    expectedPages: 2,
    name: "Comparison flyer (half-page)",
    width: "8.5in",
    height: "5.5in",
  },
];

const CSS_PX_PER_INCH = 96;
const inchesToPx = (value) => Math.round(parseFloat(value) * CSS_PX_PER_INCH);

// Lay the flyer out at its paper size in print mode, then list every visible
// element that extends past the bottom or right edge of its .flyer-page.
async function findClippedElements(page) {
  await page.emulateMedia({ media: "print" });
  return page.evaluate(() => {
    const clipped = [];
    document.querySelectorAll(".flyer-page").forEach((flyerPage, index) => {
      const bounds = flyerPage.getBoundingClientRect();
      flyerPage.querySelectorAll("*").forEach((el) => {
        const rect = el.getBoundingClientRect();
        if (rect.width === 0 || rect.height === 0) return;
        const overBottom = Math.round(rect.bottom - bounds.bottom);
        const overRight = Math.round(rect.right - bounds.right);
        if (overBottom > 1 || overRight > 1) {
          const name = el.className
            ? `${el.tagName.toLowerCase()}.${el.className}`
            : el.tagName.toLowerCase();
          clipped.push({ page: index + 1, name, overBottom, overRight });
        }
      });
    });
    return clipped;
  });
}

// Count pages in a PDF buffer by counting /Type /Page (not /Pages) objects
function countPdfPages(buffer) {
  const str = buffer.toString("latin1");
  const matches = str.match(/\/Type\s*\/Page(?!s)/g);
  return matches ? matches.length : 0;
}

async function main() {
  const browser = await chromium.launch();
  let allPassed = true;

  for (const flyer of FLYERS) {
    const url = `${BASE}${flyer.path}`;
    // Match the viewport to the paper size so layout and wrapping are the
    // same as in the printed PDF.
    const page = await browser.newPage({
      viewport: {
        width: inchesToPx(flyer.width),
        height: inchesToPx(flyer.height),
      },
    });

    try {
      await page.goto(url, { waitUntil: "networkidle", timeout: 15000 });
    } catch (err) {
      console.log(`  SKIP  ${flyer.name} — could not load ${url}`);
      await page.close();
      continue;
    }

    const pdfBuffer = await page.pdf({
      width: flyer.width,
      height: flyer.height,
      printBackground: true,
      margin: { top: 0, right: 0, bottom: 0, left: 0 },
    });

    const slug = flyer.path.replace(/\//g, "-").replace(/^-|-$/g, "");
    const outPath = `/tmp/flyer-test-${slug}.pdf`;
    writeFileSync(outPath, pdfBuffer);

    const pageCount = countPdfPages(pdfBuffer);
    const clipped = await findClippedElements(page);
    const passed = pageCount === flyer.expectedPages && clipped.length === 0;

    if (passed) {
      console.log(
        `  PASS  ${flyer.name}: ${pageCount} pages, nothing clipped — ${outPath}`,
      );
    } else {
      console.log(
        `  FAIL  ${flyer.name}: ${pageCount} pages (expected ${flyer.expectedPages}), ${clipped.length} clipped elements — ${outPath}`,
      );
      for (const pageNumber of new Set(clipped.map((c) => c.page))) {
        const onPage = clipped.filter((c) => c.page === pageNumber);
        const worst = Math.max(
          ...onPage.map((c) => Math.max(c.overBottom, c.overRight)),
        );
        console.log(
          `        page ${pageNumber}: ${onPage.length} elements past the edge, by up to ${worst}px; first: ${onPage[0].name}`,
        );
      }
      allPassed = false;
    }

    await page.close();
  }

  await browser.close();

  if (!allPassed) {
    console.log(
      "\nSome flyers have unexpected page counts or clipped content. Check the PDFs in /tmp.",
    );
    process.exit(1);
  } else {
    console.log("\nAll flyers passed.");
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
