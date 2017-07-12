# -- coding: utf-8 --
#raw_input = input in python3

print("how old are you?"),
age = input()
print("how tall are you?"),
height = input()
print("how much do you weigh?"),
weight = input()

print("So, you're %r old,%r tall and %r heavy."%(age,height,weight))

#Print with Keyword Parameter sep
person = input('Enter your name:')
print('hello',person,'!',sep=' ')

#format string{} (similiar to \s)
person = input('Enter your name:')
greeting = 'hello,{}!'.format(person)
print(greeting)

x=int(input("Enter an integer:"))
y=int(input("Enter another integer:"))
sum = x+y
sentence='The sum of {} and {} is {}.'.format(x,y,sum)
print (sentence)

#use {{ to keep {
a = 5
b = 9
setstr='the set is {{{},{}}}.'.format(a,b)
print(setstr)

#{0}，{1} indicate the sequence
x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))
setstr='{0}+{1}={2};{0}*{1}={3}.'
sentence=setstr.format(x,y,x+y,x*y)
print(sentence)
