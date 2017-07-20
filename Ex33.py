# -- coding: utf-8 --
'''
For-loop is a better choice 
make sure you will reach a False in the end (Infinite loop)
print out the result if you are not sure about the output
'''

i = 0 
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1 
    print("Numbers now:", numbers)
    print("At the bottom i is %d" % i)

print("The numbers:")

for num in numbers: 
    print(num)
    
#Use for-loop 
j = input('<')
numbers = []

for i in range(0,int(j)):
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1 #keep i = i +1 in the for-loop only cause the bottom i to become i+1, but make no difference to the list [numbers]
    print("Numbers now:", numbers)
    print("At the bottom i is %d" % i)


    
