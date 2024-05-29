#!/usr/bin/env python3

from time import sleep

l = []
for i in range(0,108):
    l.append('\033[' + str(i) + 'm')

for index in range(len(l)):
    print(f'Index: {index}, Value: {l[index]}' + '\\' + '033' + '[' + f'{index}' + 'm' + '\033[0m')
    #sleep(1)

