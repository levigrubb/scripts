#!/usr/bin/env python3

class MyClass:

   def funcOne(self):
      print('function one')
      return self

   def funcTwo(self):
      print('function two')
      return self

one = MyClass.funcOne('this')
two = MyClass.funcTwo('that')

print('in between')

print(one)
print(two)

# the below doesn't work
#three = MyClass.funcOne(one).funcTwo(two)
#print("I'm printing",three)
