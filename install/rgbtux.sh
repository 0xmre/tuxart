#!/bin/sh

if [ -z $1 ]
then
  echo "pas de parametre"

else
  mkdir -p tuxRGB
  cd $1
  make allyesconfig
  cd -
  mv $1/.config tuxRGB/allyes.config
  python3 main.py tuxRGB/allyes.config
  mv tux_mod.svg tuxRGB/redtux.svg

  cd $1
  make allnoconfig
  cd -
  mv $1/.config tuxRGB/allno.config
  python3 main.py tuxRGB/allno.config
  mv tux_mod.svg tuxRGB/bluetux.svg

  cd $1
  make allmodconfig
  cd -
  mv $1/.config tuxRGB/allmod.config
  python3 main.py tuxRGB/allmod.config
  mv tux_mod.svg tuxRGB/greentux.svg

fi
