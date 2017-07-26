
#Object oriented programming: using class
stuff = ['Test','This','Out']
print(''.join(stuff))
#stuff here is a list class,'' is a string class

class TheThing(object):

#self is a special factor, then we can use a.some_function()~some_function(a)
#self will make your fuction be used under any condition
#__init__ is the way to set internal factor

    def __init__(self):
        self.number = 0



    def some_function(self):
        print("I got called.")



    def add_me_up(self,more):
        self.number += more
        return self.number



#two different things
a = TheThing()
b = TheThing()

a.some_function()
b.some_function()

print(a.add_me_up(20))
print(a.add_me_up(20))
print(b.add_me_up(30))
print(b.add_me_up(30))

print(a.number)
print(b.number)
