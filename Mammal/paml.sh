#!/bin/bash

module load PAML

for d in */ ; do

NAME=$(echo "$d" | sed 's:/*$::')
D=$(echo "$d" | tr '[:upper:]' '[:lower:]')
TRIMMED=$(echo "$D" | sed 's:/*$::')
echo $TRIMMED	

cd $d

codeml ${TRIMMED}.ctl

cd ..

done

