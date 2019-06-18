#!/bin/sh

if [ -z $1 ]
then
  echo "pas de parametre"

else
  mkdir -p tuxRGB
  if [ "$(ls -A tuxRGB/)" ]; then rm tuxRGB/*; fi
  cd $1
  make allyesconfig
  mv .config allyes.config

  make allnoconfig
  mv .config allno.config

  make allmodconfig
  mv .config allmod.config

  cd -
  mv $1/allyes.config tuxRGB/
  mv $1/allno.config tuxRGB/
  mv $1/allmod.config tuxRGB/

  python3 main.py tuxRGB/allyes.config
  mv tux_mod.svg tuxRGB/redtux.svg

  python3 main.py tuxRGB/allno.config
  mv tux_mod.svg tuxRGB/bluetux.svg

  python3 main.py tuxRGB/allmod.config
  mv tux_mod.svg tuxRGB/greentux.svg

  cairosvg tuxRGB/redtux.svg -o tuxRGB/redtux.png
  cairosvg tuxRGB/greentux.svg -o tuxRGB/greentux.png
  cairosvg tuxRGB/bluetux.svg -o tuxRGB/bluetux.png
  cd tuxRGB
  montage -density 300 -geometry +5+50 -border 5 *.png elemenTux.png
  display elemenTux.png &


fi
