#!/usr/bin/python3

list = []
math = 0
S = 'string'

for char in S:
    list.append(ord(char))

for num in list:
    math = math + num

print('list:    ',list)
print('math ',math)

newlist = []

for item in S:
    newlist.append(map(ord,S))

print('newlist:   ', newlist)

otherlist = [ord(c) for c in S]

print('otherlist:   ',otherlist)
