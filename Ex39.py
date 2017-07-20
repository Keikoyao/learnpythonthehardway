ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while len(stuff)!= 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print("There's %d items now." %len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])#whoa!fancy
#pop()delete the last one in the list and return it. 
print(stuff.pop())
#' '.join(things) = join(' ',things)
print(' '.join(stuff)) #Join the words together into one list
print('#'.join(stuff[3:5])) 

#类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
#面向过程：根据业务逻辑从上到下写垒代码
#函数式Functional Programming：将某功能代码封装到函数中，日后便无需重复编写，仅调用函数即可
#面向对象Object Oriented Programming：对函数进行分类和封装
