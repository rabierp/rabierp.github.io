#/usr/bin/bash
pelican content -o output -s pelicanconf.py
git push -u origin pelican
ghp-import -b pelican output
git push git@github.com:rabierp/rabierp.github.io.git pelican:master
