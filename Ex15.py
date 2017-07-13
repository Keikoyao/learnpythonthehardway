# -- coding: utf-8 --
from sys import argv

script,filename = argv

txt = open(filename)

txt.close()

print("Here is your file %r:" % filename)
print (txt.read())

print ("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print (txt_again.read())

#remember to close the file when you are done 
txt_again.close()
