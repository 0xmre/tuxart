#!/bin/sh

if [ -z $1 ]
then
  echo "pas de parametre"
  for i in `seq 1 2`;
  do
    mkdir -p example$i
    cd linux-4.13.3
    make randconfig
    cd ..
    cp linux-4.13.3/.config example$i/.config
    python main.py example$i/.config
  done
else
  echo "parametre : "$1
fi
