#!/bin/sh

if [ -d TuxGallery/ ]
then
  rm -r TuxGallery
fi
if [ -d PersonalTux/ ]
then
  rm -r PersonalTux
fi
if [ -d CustomTux/ ]
then
  rm -r CustomTux
fi
if [ -d tuxRGB/ ]
then
  rm -r tuxRGB/
fi
if [ -d __pycache__/ ]
then
  rm -r __pycache__/
fi

rm *.pyc
