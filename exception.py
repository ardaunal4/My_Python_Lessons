import logging
import time
# an exception is an object with a description of what went wrong and a trace back of where the problem occured

#Exception Clauses
""" Schematic

try:
    #runs first
    # < code >
except:
    # Runs if exception occurs in try block
    < code >
else:
    # Executes if try block *succeeds*
    < code >
finally:
    # This code always executes
    < code >
"""
# Return a function that reads binary file and returns data
# Also measure time required

#Create logger
logging.basicConfig(filename = "/home/arda/Desktop/Code_Examples/problems.Log", level = logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """ Return the contents of the file at 'path' and measure time required. """
    start_time = time.time()
    try:
        f = open(path, mode = 'rb')
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info("Time required for {file} = {time}".format(file = path, time = dt))

#test code:
data = read_file_timed("maraba")
