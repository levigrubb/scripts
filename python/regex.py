#!/usr/bin/python3

import subprocess
import re
import time

ifconfig = subprocess.Popen(['ifconfig'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]

regular_exp = re.findall('[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}:[0-9a-f]{2}', str(ifconfig))
time.sleep(2)

print(regular_exp)
time.sleep(1)

for item in regular_exp:
    print(item)
    integer = int(item[-2:],16)
    print(integer)
    time.sleep(1)
    int_length = len(str(integer))
    if int_length < 2:
        new_int = str('0' + str(integer))
    elif int_length >= 2:
        new_int = str(integer)
    else:
        print('something other than the "elif" happened. Just keep going...')
    print(new_int)

