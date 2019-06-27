#!/bin/bash

OS=`lsb_release -si | tr '[:upper:]' '[:lower:]'`	#Retrieve name of OS release

declare -A osInfo;					#Retrieving default package manager
osInfo[/etc/redhat-release]=yum
osInfo[/etc/arch-release]=pacman
osInfo[/etc/gentoo-release]=emerge
osInfo[/etc/SuSE-release]=zypp
osInfo[/etc/debian_version]=apt

for f in ${!osInfo[@]}
do
    if [[ -f $f ]];then
        var="${osInfo[$f]}"		
	
    fi
done

if [ ! $# = 1 ]						#Testing numbers of passed parameters
then
	echo "Wrong number of parameters, please use -h or --help for info"
	exit 1

elif [ "$1" = "--help" ] || [ "$1" = "-h" ];		#Help
then	
	echo ""
	echo "# To use script you have to be root usr : sudo su "
	echo "# Format goes like this ./tuxsplash PATH/tux.png " 
	echo "# If you want to find your generated tux from tuxArt go to ~/Pictures" 
	exit 1

elif [ ! -f $1 ]					#Checking if file exist
then
	echo "File does not exist or wrong option, please use -h or --help for info" 
	exit 1
fi

echo "This script will save your LAST splash logo as old-splash.png, and requires root usr."
echo "Do you wish to continue ? (y/n) " 

read res

if [ "$EUID" -ne 0 ]					#Checking if user is root
then 
	echo "You are not logging in root usr"
	exit 1

elif [ $res = "y" ]					#Checking if user wish to proceed
then
	
	cairosvg $1 -o ~/Pictures/tuxsplash.png		#Making png copy of svg tux in Picture directory

	cd /usr/share/plymouth/themes/*-logo
	mv *-logo.png old-splash.png 
	cp ~/Pictures/tuxsplash.png ./$OS-logo.png
	echo "This may take a few seconds please be patient and wait =)"
	update-initramfs -u
	

fi

exit 1
