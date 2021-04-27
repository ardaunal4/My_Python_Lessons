# For more available functions use this : dir(dict)
student_grades = {"Marry": 55, "Murat": 85, "Halime": 77}

post = {"message" : "SOS Help!", "type" : "5D 4A 35M", "location" : (44.592, -15.45646)}
print(post)

post2 = dict(message = "Hey", language = "English", style = 22)
print(post2)

post2["User_id"] = 209
post2["Created_by"] = "Arda"
print(post2)
print(post2['message'])

#If there is no such a key, code will give an error. We can avoid this error by using try and except
#method such as:
try:
    print(post2['location'])
except KeyError:
    print("There is no such a key. Please insert in a valid one! ")

loc = post2.get('location', None) #If there is no location function in the dictionary, code will return None

for key in post2.keys():
    value = post2[key]
    print(key, " = ", value)

for key,value in post2.items():
    print(key, " = ", value)
