#!/bin/sh

if [ -z $1 ]
then
  echo "No .config file specified..."
  sleep 1
  echo  "Now looking for your configuration file..."
  echo
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
  sleep 1
  echo "Your personal Tux is getting assembled..."
  python3 main.py PersonalTux/.config
  mv tux_mod.svg PersonalTux/tux_mod.svg
  echo "Come and see me in PersonalTux folder!"
  display PersonalTux/tux_mod.svg &
else
  mkdir -p CustomTux
  echo "Creating your tux based on : "$1
  python3 main.py $1
  mv tux_mod.svg CustomTux/
  echo "Come and see me in CustomTux folder!"
  display CustomTux/tux_mod.svg &
fi
