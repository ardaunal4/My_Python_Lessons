import math
import statistics

def area(r):
    """ Area of a circle with radius 'r' """
    return math.pi*r**2

# if you have list of radius

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method

areas1 = []
for r in radii:
    a = area(r)
    areas1.append(a)

print(areas1)

# Method 2 : Use 'map' function

areas2 = list(map(area, radii))
print(areas2)
""" general usage style of map function:
    data = a1, a2, a3, ..., an
    Function : f
    map(f, data):
         returns  iterator over
         f(a1), f(a2), ..., f(an)  """

#use map function with the help of lambda

temps = [('Ankara', 5), ('Gaziantep', -8), ('Erzurum', -15), ('Antalya', 20)]

cs_to_fh = lambda data: (data[0], (9/5)*data[1] + 32)

result_in_fh = list(map(cs_to_fh, temps))
print(result_in_fh)

""" Filter function is used to select certaion pieces of data from list, tuple or other collection of data """

data =  [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

# we use filter to chose data elements which are highest than the mean in data
list_of_elemets = list(filter(lambda x: x > avg, data))
print(list_of_elemets)
