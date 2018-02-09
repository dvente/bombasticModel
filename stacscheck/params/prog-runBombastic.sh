#!/bin/bash

cat > stacscheck-test.param
if ! savilerow-hg Bombastic.eprime stacscheck-test.param -run-solver -solutions-to-stdout > savilerow-output 2>&1 ; then
    echo savilerow-output
fi;

cat savilerow-output | grep -E 'letting move(Col|Row) be' | sort

rm -f stacscheck-test.param
rm -f stacscheck-test.param.minion
rm -f stacscheck-test.param.info
rm -f stacscheck-test.param.infor
rm -f savilerow-output