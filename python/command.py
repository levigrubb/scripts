#!/usr/bin/python3

import subprocess

command = input('cmd: ')

if ';' in command:
    init_cmd_list = command.split(';')
    for item in init_cmd_list:
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]
else:
        output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).communicate()[0]

better_output = output.strip()
real_output = better_output.decode()

print(real_output)
