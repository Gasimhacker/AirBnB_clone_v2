#!/bin/bash
res="ls -ltr versions/"
wanted="$res| tail -n $1"
for (x in $res)
do
	if [ !x in wanted ]
