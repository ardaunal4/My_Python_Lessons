#bin() Returns binary version of given number
print(bin(4))

#enumerate() Takes a collection (e.g. a tuple) and returns it  as an enumerate object
renkler = ["sari", "kirmizi", "yesil", "blue", "black"]
x = list(enumerate(renkler))    
for index, color in x:
    print(index, color)

#reversed() change list queue to reverse 
y = [1, 45, 6, 15, 19, 66, 25]
y_prime = list(reversed(y))
print(y_prime)

#round() rounds given number
print(round(2.8))
print(round(2.3))

#sorted() sorts any collection
print("sorted y = ", sorted(y))
print("reverse sorted y = ", sorted(y, reverse = True))

#zip returs an iterator, from two or more iterators

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
print(list(zip(list1, list2)))