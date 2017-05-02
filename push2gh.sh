#/usr/bin/bash
pelican content -o output -s publishconf.py
git push -u origin pelican
ghp-import -b master output
git push git@github.com:rabierp/rabierp.github.io.git master:master
