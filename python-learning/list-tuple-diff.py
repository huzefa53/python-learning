#!/usr/bin/python

''' Tuples can be thought of as read-only lists Following is invalid with tuple, because we attempted to update a tuple, which is not allowed. Similar case is
possible with lists:'''

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tuple[2] = 1000 # Invalid syntax with tuple
list[2] = 1000 # Valid syntax with list
