#!/bin/bash

cp "${TESTDIR}/Bombastic1_1.param" stacscheck-test-basic.param &&
../savilerow Bombastic.eprime stacscheck-test-basic.param -run-solver &&
rm -f stacscheck-test-basic.param*
