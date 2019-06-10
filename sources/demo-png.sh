#!/bin/sh
NBTUX=5
echo -e "Generating random kernels from: "$1
echo

if [ -d $1 ]
then
  mkdir -p TuxGallery
  if [ -z $2 ]
  then
    echo -e "No number of random Tux specified, now generating 5 random Tux..."
    echo
  else
    echo -e "Now generating $2 Tux!"
    echo
    if [ $2 -gt 0 ]
    then
      NBTUX=$2
    else
      echo -e "Only non negative numbers are allowed!"
      sleep 1
    fi
  fi
  for i in `seq 1 $NBTUX`;
  do
    echo -e "Tux n$i is preparing..."
    echo
    cd $1
    make randconfig
    cd -
    mv $1/.config TuxGallery/.config$i
    python3 main.py TuxGallery/.config$i
    mv tux_mod.svg TuxGallery/tux_mod$i.svg
    cairosvg TuxGallery/tux_mod$i.svg -o TuxGallery/tux_mod$i.png
  done
  echo "Generating .png grid..."
  cd TuxGallery
  montage -density 300 -tile 2x0 -geometry +5+50 -border 10 *.png TuxFamily.png
  sleep 1
  echo "TuxFamily.png is now available! Check tuxart/TuxGallery folder"
fi
