"""
It is possible define of Big O as a direct function such as O(2n), O(n+5), O(2*exp(2^n)).
One of these scenarios, O(2n) still has linear relationsip with # of inputs, but its  slope is incerased. 
This 2 or +1(in O(n+1)) is called as insignifant constant and it could ignorable.
"""

# This is the exmple of O(2n)
def linear_big_o(my_list):

    for element in my_list:
        print(element)
        
    for element in my_list:
        print(element)

# And this is the example of O(n+1) 
def linear_big_o_2(my_list):

    print(my_list[0])

    for element in my_list:
        print(element)
