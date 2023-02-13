#!/usr/bin/env python3
# original source from https://github.com/guardianproject/info/blob/master/setup-pages-for-supported-languages.py

import glob
import os
import re
import shutil
import sys
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as fp:
    #config = yaml.load(fp)
    config = yaml.load(fp, Loader=SafeLoader)

rootfiles = dict()
languages = config['languages'].keys()
localized_pat = re.compile(r'.+\.([a-z][a-z](|-[A-Z][A-Z]|-Han[st]))$')

for root, dirs, files in os.walk('content'):
    #if root.startswith('content/blog'):
    #    continue  # skip since it is not translated
    for f in files:
        fileroot, extension = os.path.splitext(f)
        if extension == '.md':
            m = localized_pat.match(fileroot)
            if m:
                lang = m.group(1)
                if lang in languages:
                    #print(f, '\t', m.group(1))
                    filename = os.path.join(root, f.replace('.' + lang + '.md', '.md'))
                    if not filename in rootfiles:
                        rootfiles[filename] = []
                    rootfiles[filename].append(lang)
                    continue
            for lang in languages:
                lang_file = os.path.join(root, fileroot + '.' + lang + extension)
                if not os.path.exists(lang_file):
                    with open(os.path.join(root, f)) as fp:
                        contents = fp.read()
                    # for some reason, index.*.md copies need the menu entries
                    if f != 'index.md':
                        contents = re.sub(r'\naliases:.*?\n([^ ])', r'\n\1', contents, flags=re.DOTALL)
                        contents = re.sub(r'\nmenu:.*?\n([^ ])', r'\n\1', contents, flags=re.DOTALL)
                    with open(lang_file, 'w') as fp:
                        fp.write(contents)
