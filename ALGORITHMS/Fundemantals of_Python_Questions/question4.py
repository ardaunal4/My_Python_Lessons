# What are the Leading and Trailling?
# if there is a string with spaces, How you can remove those spaces from string?
# if spaces are at the begining of word,  then it is called as leading whitespace
# if spces are at the end of the word, then it is called as trailling whitespace

astring = "     arda    unal    "
print(astring.lstrip()) # remove leading spaces
print(astring.rstrip())  # remove trailling spaces
print(astring.strip()) # remove space both at end and beginning

# Change word letters to uppercase letters and lowercase letters
print(astring.upper())
print(astring.lower())

# What is continue operator!
for i in range(5):
    print(i)
    if i == 2:
        continue
    print(i)

# '//' operator returns only integer part of a float
print(10//3)

# What is membership operator?
mem_op = "ar" in "aarda"
print(mem_op)