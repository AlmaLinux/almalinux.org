#!/usr/bin/env python3
# original source from https://github.com/guardianproject/info/blob/master/setup-pages-for-supported-languages.py
"""Generate per-language placeholder copies of every content/*.md file.

For each Hugo content page that doesn't yet have a localized sibling, copy
the source file to content/<page>.<lang>.md for every language defined in
config.yaml. This ensures Hugo emits localized URLs for every configured
language, even when Weblate hasn't supplied a translation yet.

Run from the repo root. Used by the publish workflows; safe to run locally.
"""
import os

import yaml

with open('config.yaml') as fp:
    config = yaml.safe_load(fp)

# Sort longest-first so e.g. "pt-br" wins over "pt" when checking suffixes.
languages = sorted(config['languages'].keys(), key=len, reverse=True)

for root, _dirs, files in os.walk('content'):
    for f in files:
        fileroot, extension = os.path.splitext(f)
        if extension != '.md':
            continue

        # Skip files that are already localized variants (e.g. foo.de.md).
        if any(fileroot.endswith('.' + lang) for lang in languages):
            continue

        for lang in languages:
            lang_file = os.path.join(root, fileroot + '.' + lang + extension)
            if os.path.exists(lang_file):
                continue
            with open(os.path.join(root, f)) as src:
                contents = src.read()
            with open(lang_file, 'w') as dst:
                dst.write(contents)
