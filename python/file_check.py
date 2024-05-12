#!/usr/bin/env python3

import os

usr_path = str(input("Enter a directory or path to check: "))

try:
   if os.path.exists(usr_path):
      if os.path.isdir(usr_path):
         print('directory exists')
      elif os.path.isfile(usr_path):
         print('file exists')
except TypeError as error:
   print('type error occured\n',error)
