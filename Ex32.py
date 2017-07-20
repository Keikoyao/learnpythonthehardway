 #list []
hairs = ['brown','blond','red']
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
#this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)

#same as above
for fruits in fruits:
    print("A fruit of type:%s" % fruits)

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it 
for i in change: 
    print ("I got %r" % i)

#we can also build lists, first start with an empty one 
elements = []

#then use the range function to do 0 to 5 counts 
for i in range(0,6):
    print("Adding %d to the list." % i)
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too 
for i in elements:
    print("Element was: %d" % i)
    
# other function for lists
L.append(var)   #追加元素
L.insert(index,var)
L.pop(var)      #返回数组下标为index的元素，并从列表中删除之 pop()从最后一个开始删除
L.remove(var)   #删除第一次出现的该元素
L.count(var)    #该元素在列表中出现的个数
L.index(var)    #该元素的位置,无则抛异常 
L.extend(list)  #追加list，即合并list到L上
L.sort()        #排序
L.reverse()     #倒序
