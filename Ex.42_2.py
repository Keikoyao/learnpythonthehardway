mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

def apple():
    print("I AM APPLES!")
'''
import mystuff
mystuff.apple()
'''

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"

'''
#访问
import mystuff

mystuff.apple()
print(mystuff.tangerine)


#使用模块和访问字典相似
mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from the module
mystuff.tangerine # same thing, it's just a variable
'''

#有一个key=value模式的容器
#通过key从容器中获取数据

class MyStuff(object):

    def __init__ (self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

    

#为什么要使用类而不是仅有模块的原因：
#你可以使用Mystuff这个类，还可以用它来创建更多个Mystuff，而他们之间也不会互相冲突。
#当你导入一个模块时，你的整个项目也就只有一个这个模块。

#类似import module,实例化class来调用
thing = MyStuff()
thing.apple()
print(thing.tangerine)

#dict style 
mystuff['apple']
'''
#module style
mystuff.apple()
print(mystuff.tangerine)
'''
#class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)

class Song(object):

    def __init__ (self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()



