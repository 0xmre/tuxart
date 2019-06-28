#!/bin/bash

OS=`lsb_release -si | tr '[:upper:]' '[:lower:]'`	#Retrieve name of OS release
pip3pm=`which pip3`					#Retrieve path of pip3
cairo=`which cairosvg`					#Retrieve path of cairosvg
im=`which convert`					#Retrieve path of convert part of imagemagick

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
	echo "# Wrong number of parameters, please use -h or --help for info"
	exit 1

elif [ "$1" = "--help" ] || [ "$1" = "-h" ];		#Help
then	
	echo ""
	echo "# To use script you have to be root usr : sudo su "
	echo "# Format goes like this ./tuxsplash.sh /PATH/tux.png or .svg " 
	echo "# If you want to splash your generated tux from tuxArt go to ~/Pictures" 
	exit 1

elif [ ! -f $1 ]					#Checking if file exist
then
	echo "# File does not exist or wrong option, please use -h or --help for info" 
	exit 1
fi

echo "# This script will save your LAST splash logo as old-splash.png, and requires root usr."
echo "# Do you wish to continue (y/n) ?" 

read res

if [ "$EUID" -ne 0 ]					#Checking if user is root
then 
	echo "# You are not logging in root usr"
	exit 1

elif [ $res = "y" ]					#Checking if user wish to proceed
then
	if [ -z $pip3pm ]
	then
		echo "# It looks like you used this script before using the main program, to continue you need pip3"
		echo "# Would you like to proceed and install it as it's required to continue (y/n) ?"
		read var1
		if [ $var1 = "y" ]
		then
			$var install python3-pip
		else
			exit 1
		fi
		
	fi
	
	if [ -z $cairo ]
	then
		echo "# It looks like you used this script before using the main program, to continue you need cairosvg"
		echo "# Would you like to proceed and install it as it's required to continue (y/n) ?"
		read var2
		if [ $var2 = "y" ]
		then
			pip3 install cairosvg
		else
			exit 1
		fi
	fi 
	
	if [ -z $im ]
	then
		
		$var install imagemagick
		
	fi 


	if [[ $1 == *.png ]]
	then 
		convert $1 -resize "140x165" -quality 100 $1
		cd /usr/share/plymouth/themes/*-logo            
		mv *-logo.png old-splash.png 
		cp $1 ./$OS-logo.png
		echo "This may take a few seconds please be patient and wait =)"
		update-initramfs -u
	fi
	
	if [[ $1 == *.svg ]]
	then 	
		cairosvg -s 0.50 $1 -o ~/Pictures/tuxsplash.png		#Making png copy of svg tux in Picture directory
		cd /usr/share/plymouth/themes/*-logo            
		mv *-logo.png old-splash.png 
		cp ~/Pictures/tuxsplash.png ./$OS-logo.png
		echo "This may take a few seconds please be patient and wait =)"
		update-initramfs -u
	fi

fi

exit 1
