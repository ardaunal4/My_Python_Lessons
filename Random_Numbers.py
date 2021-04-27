""" Warning : The pseudo-random generators of this module should not be used for security purposes. Use 
os.urandom() or SystemRandom if you require a cryptographically secure pseudo-random number generator """
import random
# dir(random) and help(random.random) which means in random module there is a random function

# Display random numbers between [0,1)(
for i in range(10):
    print(random.random()) # this method close the uniform distribution, because all outcomes of the random
    #function has equally chance to come

# Generate the random numbers between [3,7)
def my_Random():
    #Random scale , shift, return...
    return 4*random.random() + 3

for i in range(10):
    print(my_Random())

# There is also a builtin function in the random module which is uniform(a,b)
for i in range(10):
    print(random.uniform(3,7))

# Generate a normal distribution
for i in range(20):
    print(random.normalvariate(0,9))

# Generate a integer random distribution
for i in range(20):
    print(random.randint(1,6)) #for rolling dice

# Generate random choice in a list

outcomes = ['rock', 'paper', 'scissors']
for i in range(20):
    print(random.choice(outcomes))

