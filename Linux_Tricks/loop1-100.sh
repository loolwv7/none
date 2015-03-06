#!/bin/bash

LIMIT=100
a=1

while [ "$a" -le "$LIMIT" ]
do
  echo -n "$a"
  let "a+=1"
done
echo

((a =1))

while (( a <= LIMIT ))
do
  echo -n "$a"
  ((a +=1))
done

echo


for a in {1..10}
do 
  echo -n "$a"
done
