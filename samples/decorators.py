

def square(x: int):
    return x ** 2

square(2)


# Before decorators
def log(func):
    """Simple decorator to print result"""
    def wrapper(x: int):
        result = func(x)
        print(f"The result is: {result}")
        return result
    return wrapper

# Use decorator without syntatic sugar. Have to define `square` agagin...
square = log(square)
square(2)


# With syntatic sugar
@log # don't have to declare square multiple time...
def square(x: int):
    return x ** 2

square(2)


# Decorator with arguments
def log_times(num_times: int=0):
    def log(func):
        def wrapper(x: int):
            result = func(x)
            for index in range(num_times):
                print(f"({index}) The result is: {result}")
            return result
        return wrapper
    return log

@log_times(num_times=3)
def square(x: int):
    return x ** 2

square(2)
