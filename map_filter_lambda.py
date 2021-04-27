x = [1, 2, 3, 4, 5, 6, 7, 8]
filtered_list = list(filter(lambda x:(x%2 == 0), x)) # first variable is a function in this case it is lambda function and second variable is a list
print(filtered_list)

mapped_list = list(map(lambda x: x**2, x))
print(mapped_list)