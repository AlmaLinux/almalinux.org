import re
import os
import json

en = json.load(open('i18n/en.json'))
error = False
dict = {}

rootdir=('.')
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
                                dict[string] = string

if error:
    print(json.dumps(dict, indent=3))
    exit(1)
