#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import shutil

ignored_path = [".\\.git", ".\\.github", ".\\qr_", ".\\test", ".\\acm\\acm-backend-english-data.el",
                r".\README", r".\my_pack.py", r".\framework.png", r".\screenshot.png",
                r".\CODE_OF_CONDUCT.md", r".\acm\stardict.py", r".\core\__pycache__",
                r".\core\handler\__pycache__", r".\lsp-bridge-master"]
def main():
    try:
        os.mkdir("lsp-bridge-master")
        os.mkdir("lsp-bridge-master\\lsp-bridge-master")
    except:
        pass
    for root, dirs, files in os.walk("."):
        for d in dirs:
            dir_path = os.path.join(root, d)
            skip = False
            for x in ignored_path:
                # print(x)
                if dir_path.startswith(x):
                    skip = True
                    break
            if skip:
                continue
            try:
                os.mkdir("lsp-bridge-master\\lsp-bridge-master" + dir_path)
            except:
                pass
            
        for n in files:
            path = os.path.join(root, n)
            skip = False
            for x in ignored_path:
                # print(x)
                if path.startswith(x):
                    skip = True
                    break
            if skip:
                continue
            
            print(path)
            shutil.copy(path, "lsp-bridge-master\\lsp-bridge-master" + path)
        # print(root)
    shutil.make_archive("lsp-bridge-master", "zip", "lsp-bridge-master")
    shutil.rmtree("lsp-bridge-master")
if __name__ == "__main__":
    try:
        main()
    except:
        import traceback
        traceback.print_exc()
        input()
