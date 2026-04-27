#!/usr/bin/env python3
"""Audit i18n/en.json against {{ i18n "..." }} usages in layouts/.

Adds any keys referenced by templates but missing from en.json, removes any
keys in en.json that no templates reference, and prunes the same stale keys
from every other i18n/<lang>.json so translators don't see strings the site
no longer uses.

Run with --check to exit 1 without writing — useful in CI / pre-commit.
"""
import argparse
import json
import os
import re
import sys

I18N_DIR = 'i18n'
EN_PATH = os.path.join(I18N_DIR, 'en.json')
TEMPLATE_DIR = 'layouts'
I18N_PATTERN = re.compile(r'{{\s+?i18n\s+?(?:"|`)(.*?)(?:"|`)\s+?}}', re.DOTALL)


def find_used_keys(template_dir):
    used = set()
    for folder, _dirs, files in os.walk(template_dir):
        for file in files:
            if not file.endswith('.html'):
                continue
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                for line in f:
                    used.update(I18N_PATTERN.findall(line))
    return used


def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def dump(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=3, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--check',
        action='store_true',
        help="Don't write changes; exit 1 if any are needed.",
    )
    args = parser.parse_args()

    en = load(EN_PATH)
    used = find_used_keys(TEMPLATE_DIR)

    missing = sorted(used - en.keys())
    unused = sorted(en.keys() - used)

    other_locales = []
    for name in sorted(os.listdir(I18N_DIR)):
        if not name.endswith('.json') or name == 'en.json':
            continue
        path = os.path.join(I18N_DIR, name)
        data = load(path)
        stale = sorted(set(data.keys()) - used)
        if stale:
            other_locales.append((path, data, stale))

    has_changes = bool(missing or unused or other_locales)

    for key in missing:
        print(f"Adding '{key}' to en.json")
    for key in unused:
        print(f"Removing '{key}' from en.json")
    for path, _data, stale in other_locales:
        print(f"{os.path.basename(path)}: pruning {len(stale)} stale key(s)")

    if args.check:
        if has_changes:
            print('\nfind_missing_i18n_strings.py would modify i18n/. Re-run without --check.')
            sys.exit(1)
        return

    if not has_changes:
        return

    for key in missing:
        en[key] = key
    for key in unused:
        del en[key]
    dump(EN_PATH, en)

    for path, data, stale in other_locales:
        for key in stale:
            del data[key]
        dump(path, data)


if __name__ == '__main__':
    main()
