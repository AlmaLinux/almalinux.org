import re
import os
import json
import argparse

# Argument parser for optional dry-run mode
parser = argparse.ArgumentParser(description='Check i18n keys in layouts.')
parser.add_argument('--write', action='store_true', help='Write changes to en.json')
args = parser.parse_args()

# Set root directory explicitly
rootdir = './layouts'

# Load en.json contents
try:
    with open('i18n/en.json', 'r', encoding='utf-8') as f:
        en = json.load(f)
except FileNotFoundError:
    print('ERROR: i18n/en.json not found.')
    exit(1)

unused_keys = set(en.keys())
error = False
missing_keys = {}

for folder, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.html'):
            fullpath = os.path.join(folder, file)
            try:
                with open(fullpath, 'r', encoding='utf-8') as f:
                    for line in f:
                        m = re.findall(r'{{\s+?i18n\s+?(?:"|`)(.*?)(?:"|`)\s+?}}', line, re.DOTALL)
                        if m:
                            for string in m:
                                if string not in en:
                                    error = True
                                    print(f'TRANSLATION ERROR: {string}')
                                    missing_keys[string] = ''
                                    en[string] = string  # Add missing key
                                elif string in unused_keys:
                                    unused_keys.remove(string)
            except Exception as e:
                print(f'ERROR reading {fullpath}: {e}')

# Report unused keys
if unused_keys:
    print('Unused keys:')
    for key in unused_keys:
        print(f" - {key}")

# Write changes if requested
if args.write:
    try:
        # Remove unused keys
        for key in unused_keys:
            del en[key]
        with open('i18n/en.json', 'w', encoding='utf-8') as f:
            json.dump(en, f, indent=3, ensure_ascii=False)
        print('en.json updated.')
    except Exception as e:
        print(f'ERROR writing en.json: {e}')
else:
    print('Dry-run mode: No changes written. Use --write to apply changes.')

