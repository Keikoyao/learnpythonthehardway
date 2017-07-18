# -- coding: utf-8 --
from sys import argv
script, input_file = argv

#read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
def print_all(f):
    print (f.read())

#seek() 移动文件读取指针到指定位置
def rewind(f):
    f.seek(0)

#readline() will read the file line by line as if there is a for next loop automatically vs readlines()一次读取整个文件
def print_a_line(line_count,f):
    print (line_count,f.readline())

current_file = open(input_file)
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1 
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += current_line + 1
print_a_line(current_line,current_file)
