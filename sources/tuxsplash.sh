#!/bin/bash
y="y"
n="n"

help="-help"
OS=`lsb_release -si | tr '[:upper:]' '[:lower:]'`


if [ "$1" = $help ]
then	
	echo "To use script you have to be root usr : sudo su"
	echo "Parameters goes : " 
	echo "./tuxsplash (~/logo.png)" 
	exit 1
fi

echo "This script will save your LAST splash logo as old-splash.png, and requires root usr."
echo "Do you wish to continue ? (y/n) " 

read res

if [ "$EUID" -ne 0 ]
then 
	echo "You are not logging in root usr, now exiting."
	exit 1
elif [ ! $# = 1 ]
then
	echo "Parameters are wrong, now exiting."
	exit 1
elif [ $res = $y ]
then
	cd /usr/share/plymouth/themes/*-logo
	mv *-logo.png old-splash.png 
	cp $1 ./$OS-logo.png
	update-initramfs -u
	

fi

exit 1
