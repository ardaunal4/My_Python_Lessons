# Alkaline Earth Metals

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

#by using sort method, we sort them alphabetically
earth_metals.sort()
print(earth_metals)
# if you want to reverse it
earth_metals.sort(reverse= True)
print(earth_metals)

#if we wanna sort to tuples, we can use sorted function

data = (3, 4, 1, 7, 5, 9, 2, 10, 6, 8) # although data is tuple, after sorted method it will be a list!
print(sorted(data))