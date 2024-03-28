#!/bin/bash
touch $1.txt
touch $1.sample.txt
touch $1.py
printf "# input = open(\"%s.txt\", \"r\").readlines()\n" $1 >> $1.py
printf "input = open(\"%s.sample.txt\", \"r\").readlines()\n" $1 >> $1.py
printf "p1 = 0\n" >> $1.py
printf "p2 = 0\n" >> $1.py