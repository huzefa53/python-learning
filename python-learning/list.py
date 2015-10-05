#!/usr/bin/python

''' Lists are the most versatile of Python's compound data types. A list contains items separated by commas and
enclosed within square brackets ([]). To some extent, lists are similar to arrays in C. One difference between them
is that all the items belonging to a list can be of different data type.
The values stored in a list can be accessed using the slice operator ( [ ] and [ : ] ) with indexes starting at 0 in the
beginning of the list and working their way to end -1. The plus ( + ) sign is the list concatenation operator, and the
asterisk ( * ) is the repetition operator. For example:'''

list = [ 'huzefa', 'hamdard', 786, '22.43' ]
tinylist = [122, 'huzefa' ]

print list         #print complete list
print list[0]      #print first element of list
print list[1:3]   # print from first to third element of list
print list [2:]   #print elements starting from 3rd element
print tinylist * 2  #print list 2 times
print list + tinylist  #print concateneted list
