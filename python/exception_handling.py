#!/usr/bin/env python3

try:
   numerator = int(input('enter a number to divide: '))
   denominator = int(input("enter a number to divide by: "))
   result = numerator / denominator
except ZeroDivisionError as e:
   print("That's not a number")
   print(e)
except ValueError as e:
   print("only numbers can be divided")
   print(e)
except Exception as e:
   print("Something else occurrec")
   print(e)
else:
   print(result)
finally:
   print('this will always execute')
   