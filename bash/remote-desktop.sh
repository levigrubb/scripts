#!/bin/bash
# This script will create a more user-friendly RDP experience

args=($1 $2 $3 $4 $5 $6 $7 $8)

read -p 'IP Address:' ip
read -p 'Username: ' username
read -s -p "Password: " password

xfreerdp +clipboard /cert:ignore /u:$username /p:$password /w:1920 /h:1000 /v:$ip

