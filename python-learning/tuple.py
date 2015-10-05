#!/usr/bin/python

''' A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated
by commas. Unlike lists, however, tuples are enclosed within parentheses.
The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and
size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be
thought of as read-only lists. For example:'''

tuple = [ 'huzefa', 'hamdard', 786, '22.43' ]
tinytuple = [122, 'huzefa' ]

print tuple       #print complete list
print tuple[0]      #print first element of list
print tuple[1:3]   # print from first to third element of list
print tuple [2:]   #print elements starting from 3rd element
print tinytuple * 2  #print list 2 times
print tuple + tinytuple  #print concateneted list
