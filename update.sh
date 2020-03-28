#!/bin/bash
git fetch upstream
git merge upstream/master
cd ..
python.exe COVID-19/custom/main.py
cd COVID-19/
git add .
git commit -m "Daily update"
git push origin master