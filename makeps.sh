#!/bin/bash

# Usage: makeps.sh /path/to/exams/

cd $1
echo "Scanning through all pythong scripts in `pwd`"
find * -type f -name \*.py | while read f ; do
    f2=`echo $f | sed -e 's/.STUDAT.CHALMERS.SE\/Assignments//'`
    n=`echo $f2 | sed -e 's/\//_/g' | sed -e 's/ /_/g' | sed -e 's/.py$//'`
	a2ps --prologue=color -1 -l 110 -s duplex -T 3 -D user.name="" --left-footer="$f2" -o "$n".ps "$f"
done
