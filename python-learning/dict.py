#!/usr/bin/python

'''Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and
consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings.
Values, on the other hand, can be any arbitrary Python object.
Dictionaries are enclosed by curly braces ( { } ) and values can be assigned and accessed using square braces (
[] ). For example:'''

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name':'huzefa', 'age':26, 'job':'IT'}

print dict['one']  #prints value for 'one' key
print dict[2]    #print values for 2 key
print tinydict   #print complete timydict
print tinydict.keys()  #print all the keys
print tinydict.values() #print all the values
