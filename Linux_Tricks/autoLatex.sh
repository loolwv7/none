#!/bin/bash -x
#tex='ls ./ | grep tex | 'awk {print $2}''
tex=`find . -maxdepth 1 -name "*.tex"`
#if [ $tex = "tex" ] ; then
if [ $tex != "" ] ; then
latex $tex
else
	exit 0
fi
