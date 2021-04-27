# What is args and kwargs?

# args is useful when we define a function, but we do not want to specify number of inputs of this funtion.
def args_func(*args):

    for each in args:
        print(each)

args_func(1, 2, 3)
# kwargs has a same functionality, but it is dictionary version of args

def kwargs_func(**kwargs):
    
    for each in kwargs:
        print(each, kwargs[each])

kwargs_func(a = 1, b = 1, c = 3)
