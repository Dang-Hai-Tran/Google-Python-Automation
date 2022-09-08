#!/bin/bash

touch oldFiles.txt
files_Jane=$(grep " jane " ../data/list.txt | cut -d " " -f 3)
for  file in $files_Jane; do
    if test -e ../$file; then
        echo $file >> oldFiles.txt;
    fi;
done;

