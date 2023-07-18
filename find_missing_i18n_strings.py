import re
import os
import json

# Open the json file and load its contents into a dictionary
with open('i18n/en.json', 'r') as f:
    en = json.load(f)

# Create a copy of the en dictionary's keys and convert it to a set for better performance
unused_keys = set(en.keys())

error = False
missing_keys = {}

rootdir = '.'
# TODO: Crawl only content/*
for folder, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.html'):
            fullpath = os.path.join(folder, file)
            with open(fullpath, 'r') as f:
                for line in f:
                    m = re.findall('{{\s+?i18n\s+?(?:"|`)(.*?)(?:"|`)\s+?}}', line, re.DOTALL)
                    if m:
                        for string in m:
                            if string not in en:
                                error = True
                                print(f'TRANSLATION ERROR: {string}')
                                missing_keys[string] = ''
                                en[string] = string  # Add the missing key to the dictionary with an empty value
                            elif string in unused_keys:
                                unused_keys.remove(string)

# If there are missing keys, dump the updated dictionary back into the json file
if error:
    print(json.dumps(missing_keys, indent=3))
    with open('i18n/en.json', 'w') as f:
        json.dump(en, f, indent=3)  
    exit(1)

# If there are unused keys, print them
# TODO: Do something useful?
if unused_keys:
    print("UNUSED KEYS:")
    for key in unused_keys:
        print(key)
else:
    print("No unused keys found.")

