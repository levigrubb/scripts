#!/usr/bin/python3

import argparse

file_passed = argparse.ArgumentParser()
arg_file = file_passed.parse_args("file", type=str, help='the file that that you put int')

