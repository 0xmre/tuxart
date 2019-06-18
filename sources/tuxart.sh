#!/bin/sh

val=0
total=15000
if [ -z $1 ]
then
  echo "No .config file specified..."
  echo
  sleep 1
  echo  "Now looking for your configuration file..."
  sleep 1
  mkdir -p PersonalTux
  cat /boot/config-$(uname -r) > PersonalTux/.config
  if [ $? -ne 0 ]
  then
    echo ".config not found in /boot, trying in /proc"
    zcat /proc/config.gz > PersonalTux/.config
    if [ $? -ne 0 ]
    then
      echo "/proc/config.gz not found, try passing .config file manually with './tuxart.sh [filename]'"
    fi
  fi
  echo
  echo "Configuration file has been found!"
  echo
  sleep 1
  echo "Your personal Tux is getting assembled..."
  echo
  sleep 1
  python3 main.py PersonalTux/.config
  VAR=`cat .env`
  val=`echo "$VAR/$total" | bc`
  echo $val
  convert -implode `echo "$VAR/$total" | bc` tux_mod.svg tux_mod.png
  mv tux_mod.svg PersonalTux/tux_mod.svg
  echo "Come and see me in PersonalTux folder!"
  display tux_mod.png
  #display PersonalTux/tux_mod.svg &
else
  mkdir -p CustomTux
  echo "Creating your tux based on : "$1
  python3 main.py $1
  mv tux_mod.svg CustomTux/
  echo "Come and see me in CustomTux folder!"
  display CustomTux/tux_mod.svg &
fi
