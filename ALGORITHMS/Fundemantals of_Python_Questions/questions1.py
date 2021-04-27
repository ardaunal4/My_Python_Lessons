import copy

# What is the difference between deep copy and shallow copy?
# What is the deep copy: Deep copy is using for the copy an old list to new one and break the connection between them.
# So when you change an element of the old list, it will not reflect to new list.
old_list = [1, 2, 3, 4, 5, 6]
new_list = copy.deepcopy(old_list)
print("Before Old list : ", old_list)
print("Before New list : ", new_list)
old_list[2] = 10
print("After Old list : ", old_list)
print("After New list : ", new_list)

# Shallow copy does same thing, but after shallow copy old and new lists are connected. When you change the old list, new list will be effected.
old_list = [1, 2, 3, 4, 5, 6]
new_list = copy.copy(old_list)
print("Before Old list : ", old_list)
print("Before New list : ", new_list)
old_list[2] = 10
print("After Old list : ", old_list)
print("After New list : ", new_list)

# What is the difference between list and tuple?
# List is a dynamic array. It is changeable
# The tuple is not dynamic. It is not changeble. After you define tuple, you can not change its elements!

a_list = [1, 2, 3, 4]
a_list.append(5)
a_list[2] = 20
a_list.clear()

a_tuple = (1, 2, 3, 4)
#a_tuple[2] = 12  it is gonna raise an error!