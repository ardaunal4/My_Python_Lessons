f = open('deneme.txt') #open txt file
text = f.read() # read file 
print(text)
f.close()

#Another technique to read file without close it, because it is not necessary

with open('deneme.txt') as fobj:
    bio = fobj.read()
print(bio)

# If there is no file when we try to read it, this method will be useful

try:
    with open("something.txt") as something:
        st = something.read()
except FileNotFoundError:
    pass


#how can we write a file
oceans = ["Pasific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("oceans.txt", 'w') as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

#we can append the text end of the file by using append mode

with open("oceans.txt", "a") as f: # append mode will create file if it doesn't exist, but if it exists, it will append to text
    print(23*"=",file=f)
    print("These are the 5 oceans. ", file=f)
    
    
        
