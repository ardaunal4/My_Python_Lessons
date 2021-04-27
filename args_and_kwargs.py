"""
*ARGS:
*args(arbitrary arguments) and **kwargs allow you to pass multiple arguments or keyword arguments to a function
*args usage:
def something(*args):
    return args -> result of return will be a tuple

**KWARGS :
works just like *args, but instead of accepting positional arguments it accepts keyword(or named) arguments.
It returns a dictionary
"""

def topla1(x, y, z):
    return x + y + z

result1 = topla1(3, 4, 5)
print(result1)

def topla2(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam

result2 = topla2(3, 4, 5)
print(result2)

def kimlik(**kwargs):
    for key, value in kwargs.items():
        print("{} : {} ".format(key, value))

kimlik(isim = 'name', soyisim = "surname", yas = "age", tc = 1165165646, mail = "asda@asdasd.com")

# Both of them in same func

def yeni(*args, **kwargs):
    print("args = ", args, "kwargs = ", kwargs )

yeni(1, 2, 3, 4, 5, 6, 7, isim = "mamet", soyisim = "deli", yas = 19)