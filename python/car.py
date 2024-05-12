class Car:
   
   wheels = 4

   def __init__(self,make,model,year,color):
      self.make = make
      self.model = model
      self.year = year
      self.color = color
   
   def Drive(self):
      print(self.model,'is driving')

   def Stop(self):
      print(self.model,'stopped')

   