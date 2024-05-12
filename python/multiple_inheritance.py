#!/usr/bin/env python3

class Prey:

   def flee(self):
      print("the animal is fleeing")

class Predator:
   def hunt(self):
      print('the animal hunts')


class Rabbit(Prey):
   pass


class Hawk(Predator):
   pass


class Fish(Predator,Prey):
   pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.hunt()
fish.flee()
