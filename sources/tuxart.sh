#!/bin/sh

if [ -z $1 ]
then
  echo "No .config file specified...\n"
  sleep 1
  echo  "Looking now for your configuration file...\n"
  sleep 1
  mkdir -p PersonalTux
  cat /boot/config-$(uname -r) > PersonalTux/.config
  if [ $? -ne 0 ];then
    echo ".config not found in /boot, trying in /proc"
    zcat /proc/config.gz > PersonalTux/.config
    if [ $? -ne 0 ];then
    echo "config.gz not found in /proc/config.gz, try passing .config file manually with ""./tuxart.sh [filename]\n"
  fi
fi
    echo "Configuration file has been found!\n"
    sleep 1
    echo "Your custom Tux is getting assembled...\n"
    python3 main.py PersonalTux/.config
    mv tux_mod.svg PersonalTux/tux_mod.svg
    eog PersonalTux/tux_mod.svg
else
  mkdir -p CustomTux
  echo "Currently running : "$1
  python3 main.py $1
  mv tux_mod.svg CustomTux/
  eog CustomTux/tux_mod.svg &
fi
