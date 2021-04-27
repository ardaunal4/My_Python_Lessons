#full details of the function of list finding here dir(numbers)
primes = [2, 3, 5, 7, 11, 13, 17, 19]

print(primes[0])
print(primes[-1])
print(primes[1])
print(primes[2:5])

primes.append(17)
primes.append(19)
print(primes)

example = [128, 17.5, True, 'Alpha', [6, 6, 7, 'False']]
print(example[-1])

numbers = [1, 2, 3]
names = ['a', 'b', 'c']
summation = numbers + names
print(summation)