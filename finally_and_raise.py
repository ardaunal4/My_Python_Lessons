try:
    x = int(input("Bir sayi giriniz : "))
    y = int(input("Ikinci sayiyi giriniz : "))
    print("Result = ", x/y)

except:
    print("There is a mistake!")

else:
    print("there is no mistake")

finally:
    print("This part works in  both situation.")

# if y == 0:
#     raise Exception("Please use another value of second number instead of 0!")

""" We can create a child class from exception class the specify error itself! """
class ZeroError(Exception):
    pass

if y == 0:
    raise ZeroError("Please use another value of second number instead of 0!")