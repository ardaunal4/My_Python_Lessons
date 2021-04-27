import logging #Purpose of logging : Record progress and problems
"""Look at dir(logging)
The entries which consist of capitals are called constants
If they start with capitalize, then they are called classes
If they start with lower case letter, then they are called as methods"""

#First create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "/home/arda/Desktop/Code_Examples/Lumberjack.Log", 
        level= logging.DEBUG, format = LOG_FORMAT,
        filemode = 'w')
logger = logging.getLogger() #call the get logger method to create a logger object

#Test the logger
logger.info("Our first message")

print(logger.level)
"""Levels are consist of numbers as:
        Level             Numeric Value
----------------------------------------------------------
1 -     NOTSET            0
2 -     DEBUG             10
3 -     INFO              20
4 -     WARNING           30
5 -     ERROR             40
6 -     CRITICAL          50
"""

# Test messages
logger.debug("This is a debug message. ")
logger.info("This is a info message")
logger.warning("This is warning message.")
logger.error("This is a error message.")
logger.critical("This is a critical message. ")