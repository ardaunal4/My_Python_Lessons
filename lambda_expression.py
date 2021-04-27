# or it is called as anonymous function

# write a function to compute 3x + 1
def f(x):
    return 3*x + 1

# write an anonymous function

g = lambda x : 3*x + 1

print(g(2))

# Combine first name and last name into a single "Full  Name"

full_name = lambda fn, ln : fn.strip().title() + " " + ln.strip().title()
print(full_name(" ahmet", "muZDARİp"))

# Build a quadratic funtion

def quadratic_function(a, b, c):
    """ Returns the function f(x) = a*x**2 + b*x + c """
    return lambda x: a*x**2 + b*x + c

f = quadratic_function(3, 2, -1)
print(f(0))

f = quadratic_function(3, 2, -1)(0)
print(f)


