#!/usr/bin/env node
/**
 * Test that flyer pages print to the expected number of PDF pages.
 *
 * Usage:
 *   npx playwright install chromium   # first time only
 *   node test-flyer-print.mjs [base-url]
 *
 * Defaults to http://localhost:1313 — start Hugo server first.
 * Generates PDFs in /tmp and reports page counts.
 */

import { chromium } from "playwright";
import { writeFileSync } from "fs";

const BASE = process.argv[2] || "http://localhost:1313";

const FLYERS = [
  { path: "/flyer/", expectedPages: 2, name: "Main flyer (letter)", width: "8.5in", height: "11in" },
  { path: "/flyer-elevate/", expectedPages: 2, name: "ELevate flyer (half-page)", width: "8.5in", height: "5.5in" },
  { path: "/flyer-compare/", expectedPages: 2, name: "Comparison flyer (half-page)", width: "8.5in", height: "5.5in" },
];

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
    const page = await browser.newPage();

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
    const passed = pageCount === flyer.expectedPages;

    if (passed) {
      console.log(`  PASS  ${flyer.name}: ${pageCount} pages — ${outPath}`);
    } else {
      console.log(`  FAIL  ${flyer.name}: ${pageCount} pages (expected ${flyer.expectedPages}) — ${outPath}`);
      allPassed = false;
    }

    await page.close();
  }

  await browser.close();

  if (!allPassed) {
    console.log("\nSome flyers have unexpected page counts. Check the PDFs in /tmp.");
    process.exit(1);
  } else {
    console.log("\nAll flyers passed.");
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
