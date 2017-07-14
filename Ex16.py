from sys import argv

script,filename = argv

print("We are going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#create and open the file (test.txt) in the 'write' mode, we don't need to have a test.txt file already in the directory
target = open(filename,'w')

print("Truncating the file. Goodbye!")

#clean up test.txt file
target.truncate()

print("Now I'm going to ask you for three lines.")

target.write("%s\n%s\n%s\n"%(line1,line2,line3))

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()
