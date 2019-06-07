#!/bin/sh

if [ -z $1 ]
then
  echo "No .config file specified, running now demos with random configurations..."
  mkdir -p TuxGallery
    for i in `seq 1 5`;
  do
    echo "Tux n$i is preparing..."
    cd linux-4.13.3
    make randconfig
    cd ..
    mv linux-4.13.3/.config TuxGallery/.config$i
    python3 main.py TuxGallery/.config$i
    mv tux_mod.svg TuxGallery/tux_mod$i.svg
    cairosvg TuxGallery/tux_mod$i.svg -o TuxGallery/tux_mod$i.png
  done
  echo "Generating .gif file..."
  cd TuxGallery
  convert -delay 100 -loop 0 tux_mod*.png SuperTux.gif


else
  mkdir -p PersonalTux
  echo "parametre : "$1
  python3 main.py $1
  mv tux_mod.svg PersonalTux/
  eog PersonalTux/tux_mod.svg &
fi
