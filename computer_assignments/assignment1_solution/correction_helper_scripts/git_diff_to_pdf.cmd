git diff -U100000 > pass_00.diff
enscript -f Courier7 -o pass_00.ps --color -Ediffu pass_00.diff
ps2pdf pass_00.ps
rm pass_00.diff pass_00.ps
