# If you have a big data set, you can use tuples instead of the list
import sys
import math

list_eg = [1, 2, 3, 'a', 'b', 'c', True, math.pi]
tuple_eg = (1, 2, 3, 'a', 'b', 'c', True, math.pi)

print("List size = ", sys.getsizeof(list_eg))
print("Tuple size = ", sys.getsizeof(tuple_eg))

#In list we can add, remove, and change data, but in tuple they are not!

survey = (27, 'Vietnam', True)

age = survey[0]
country = survey[1]
knows_python = survey[2]

print("Age = ", age)
print("Country = ", country)
print("Knows_python = ", knows_python)


survey2 = (21, 'Switzerland', False)
age, country, knows_python = survey2

print("Age = ", age)
print("Country = ", country)
print("Knows_python = ", knows_python)

