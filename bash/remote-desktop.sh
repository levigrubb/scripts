#!/bin/bash
# This script will create a more user-friendly RDP experience

args=($1 $2 $3 $4 $5 $6 $7 $8)

read -p 'Username: ' username
read -s -p "Password: " password

if [[ "$1" ~= "-[Ff]" ]];
then
	xfreerdp +clipboard /cert:ignore /u:$username /p:$password /w:1920 /h:1080 
fi

