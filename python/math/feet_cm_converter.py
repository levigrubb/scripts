#!/usr/bin/env python3

user_input = input('height in cm: ')

converter = float(user_input) * 0.0328084
feet = str(converter).split('.')[0]
dec_inches = float('0.' + str(converter).split('.')[1])
inches = round(12 * dec_inches)

print('feet:\t', feet)
print('inches:\t',inches)
