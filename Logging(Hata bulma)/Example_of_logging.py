import logging
import math

#Create and configure logger

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="log_example.Log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')

logger = logging.getLogger()

def quadratic_formula(a, b, c):
    """Return solutions to the equation ax^2 + bx + c = 0. """
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    #compute discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c
    #compute the roots
    logger.debug("# Compute the roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    #return the roots
    logger.debug("# Return the roots")
    return (root1, root2)


roots = quadratic_formula(1, 0, -4)
print(roots)
""" basit bir sekilde yapilan islemlerin surecini bir dosyaya yazdirmamizi sagliyor. Bu sekilde nerede hatamiz
oldugunu bulabiliyoruz, cunku hata olunca o islem gerceklestirilmediginden o mesaj dosyaya yazilmiyor! """