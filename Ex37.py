# -- coding: utf-8 --
#while-loop:when you want to loop non-stop, when you have limited target, use for-loop
#The best way to adjust your code is to print out the key variables and see what's wrong.
#run and test your code step by step, don't debug till you have a very long script. 

#Keywords
#remove the first matching value
a = [0, 2, 2, 3]
a.remove(2)
# reasult: a = [0, 2, 3]

#del removes a specific index
a = [3,2,2,1]
del a[1]
#result [3,2,1]

#pop returns the removed element
a=[4,3,5]
a.pop(1)
#result:3  a=[4,5]

#global make vairables global 
global dummy

#assert:create assertion
assert 1 == 1 
'''assert condition 相当于
   if not condition
        raise AssertionError()
'''
'''
yield
break
exec
class
raise
continue
finally
lambda

Escape Sequences
\\
\'
\"
\a
\b
\f
\n
\r
\t
\v

string Formats
%d
%i
%o
%u
%x
%X
%e
%E
%f
%F
%g
%G
%c
%r
%s
%%

operators
//
()
[]
{}
@
;
//=
%=
**=
'''
