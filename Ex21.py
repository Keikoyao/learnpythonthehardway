# -- coding: utf-8 --
def add(a,b):
    print("ADDING %d + %d" % (a,b))
    return a+b

def subtract(a,b):
    print("SUBTRACTING %d - %d"%(a,b))
    return a-b

def multiply(a,b):
    print("MULTPLYING %d * %d" %(a,b))
    return a*b

def divide (a,b):
    print("DIVIDING %d/%d" % (a,b))
    return a/b

print("Let's do some math with just functions")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

#add(30,5)  -- ADDING 30 + 5  When you call a function, the print content will show 
#print(age)  -- 35  When you print a function, the return value will show 
print("Age:%d, Height:%d, Weight:%d, IQ:%d"%(age, height, weight,iq))

#A puzzle for the extra credit, type it in anyway. 
print("Here is a puzzle.")

#35+74-180*25
what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes:",what, "Can you do it by hand?")
