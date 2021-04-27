# How you can convert a sorted list to random
from random import shuffle

my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print("Sorted list : ", my_list)
shuffle(my_list)
print("Shuffled list : ", my_list)

# How you can make sorted list from random list
my_list.sort()
print("Sorted list : ", my_list)

# What are functionality of the join() and split() functions
astring = "hello"
new_string = ".".join(astring) # it puts . between every latter in  the word.
print("Join() with '.' : ", new_string)
splitted_string = new_string.split(".") # Split function seperates the word according to '.'
print("Split() with '.' : ", splitted_string)
joined = "".join(splitted_string)
print("Join() after split() : ", joined)
