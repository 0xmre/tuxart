#!/bin/sh

if [ -z $1 ]
then
  echo "pas de parametre"
  for i in `seq 1 2`;
  do
    echo "Tux n$i is preparing..."
    mkdir -p example$i
    cd linux-4.13.3
    make randconfig
    cd ..
    cp linux-4.13.3/.config example$i/.config
    python main.py example$i/.config
    mv tux_mod.svg example$i/
    eog example$i/tux_mod.svg
  done
else
  echo "parametre : "$1
fi
