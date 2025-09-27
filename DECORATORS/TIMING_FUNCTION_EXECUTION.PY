# WRITE A DECORATOR THAT MEASRUES THE TIME OF A FUNCTION TAKES TO EXECUTE
import time
def timer(func ):
    def wrapper(*args):
        result=func(*args)
        return result
    return wrapper