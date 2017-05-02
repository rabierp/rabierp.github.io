#/usr/bin/bash
pelican content -o output -s pelicanconf.py
ghp-import output
git push git@github.com:rabierp/rabierp.github.io source:master
