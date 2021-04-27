#Normal list
squares = []

for i in range(1,31):
    squares.append(i**2)

print(squares)

#List Comprehension
squares2 = [i**2 for i in range(1,31)]
print(squares2)

#Another example with strings

movies = ['Geo Joe', 'Dinosoar', 'Bullshit', 'Crocodile', 'Iron Man', 'Garbage', 'Gauge',]

gmovies = []
for title in movies:
    if title.startswith('G'):
        gmovies.append(title)

# with list comprehension
gmovies = [title for title in movies if title.startswith('G') ]
print(gmovies)

#Cartesian product with list

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]
cartesian_product = [(a, b) for a in A for b in B]