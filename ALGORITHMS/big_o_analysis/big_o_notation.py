"""
When two algorithms are compared each other, it is not true to use time as a data complexity measurement.
Big O term represents growth of a function. It is a measure of time according to giving input. 
It is also called as asymptotic analysis.
It is using for comparision of two algroithms to see code complexity.
Big O test is using for the wworst case scenario in the test of an algorithm
Omega test is using for the best case scenario in the test of an algorithm
Theta test is using for mid case scenario in the test of an algorithm
Examples and types of Big O : 
"""

# Example1: Constant O(1) : It is independent from number of inputs
def constant_big_o(my_list):
    return my_list[0]

# Example1: Linear O(n) : Running time is linearly corrolated with number of inputs.
def linear_big_o(my_list):
    for element in my_list:
        print(element)

# Example1: Cubic O(n^3) : Running time is corraleted with cube of number of inputs
def cube_big_o(my_list):
    for element1 in my_list:
        for element2 in my_list:
            for element3 in my_list:
                print(element1, element2, element3)
        

def main():

    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    constant_big_o(a_list)
    linear_big_o(a_list)
    cube_big_o(a_list)

if __name__ == "__main__":
    main()
