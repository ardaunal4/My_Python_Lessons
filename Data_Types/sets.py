import math
#You can use methods with set which is finding by writing this : dir(set())

example1 = set(['hale', 45, math.pi, 66.5, 'A'])
print(example1)
#create three types of set

odds = set([1, 3, 5, 7, 9])
evens = set([0, 2, 4, 6, 8])
primes = set([2, 3, 5, 7])

intersection = odds.intersection(evens)
union = odds.union(primes)

print(intersection)
print(union)


