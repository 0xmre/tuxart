#!/bin/bash

help="-help"

if [ "$1" = $help ]
then	
	echo "To use script please use : sudo su"
	echo "Parameters goes : " 
	echo "./tuxsplash (your distrib name lower case) (~/logo.png)"
	exit 1
fi

echo "This script will save your LAST splash logo as old-splash.png, and requires root usr."
echo "Do you wish to continue ? (y/n) " 

read res

if [ "$EUID" -ne 0 ]
then 
	echo "You are not logging in root usr, now exiting."
	exit 1
elif [ ! $# = 2 ]
then
	echo "Parameters missing, now exiting."
	exit 1
elif [ $res = $y ]
then
	cd /usr/share/plymouth/themes/*-logo
	mv *-logo.png old-splash.png 
	cp $2 ./$1-logo.png
	update-initramfs -u
	

fi

exit 1
