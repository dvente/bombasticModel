#!/bin/bash
rm -f time.log
echo "file, found solution, execution time" >> time.log
find . -name "*.param" | while read line
do
	execOutput=$(TIMEFORMAT='%U'; { time ../savilerow Bombastic.eprime $line -run-solver; } 2>&1)
	echo $execOutput
	output=$line
	if grep -q solution "$execOutput"
	then
		output=$output", true, "
	else
		output=$output", false, "
	fi
	tme=$(echo $execOutput | grep -e '/(\d\.\d+)/')
	output=$output$tme
	echo $output >> time.log
done
