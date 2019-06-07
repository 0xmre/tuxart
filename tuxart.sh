#!/bin/sh
#ffnpeg
if [ -z $1 ]
then
  echo "pas de parametre"
  for i in `seq 1`;
  do
    echo "Tux n$i is preparing..."
    mkdir -p example$i
    cd linux-4.13.3
    make allnoconfig
    cd ..
    cp linux-4.13.3/.config example$i/.config
    python main.py example$i/.config
    mv tux_mod.svg example$i/
    display example$i/tux_mod.svg &
  done
else
  mkdir -p exempleperso
  echo "parametre : "$1
  python main.py $1
  mv tux_mod.svg exempleperso/
  display exempleperso/tux_mod.svg &

fi
