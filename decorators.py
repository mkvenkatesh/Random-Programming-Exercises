# A decorator is the implementation of a pattern that allows adding a behavior
# to a function or a class. It is usually expressed with the @decorator syntax
# prefixing a function.

# When the code runs, 
# 1. It hits the @some_decorator syntax and executes some_decorator(decorated_function). 
# 2. This function call returns the wraps method. 
# 3. The function call 'decorated_function(10)' is executed which calls wraps(10)
# 4. It prints "Calling function 'decorated_function'"
# 5. decorated_function((10,)) is called in wraps
# 6. decorated_function prints "With argument (10,)" and comess back to wraps and returns

def some_decorator(f, *args):
    print(f)
    def wraps(*args):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wraps

@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")

decorated_function(10)


# Decorator applied to a lambda, although a lambda can't be a decorated function

# Defining a decorator
def trace(f):
    def wrap(*args, **kwargs):
        print(f"[TRACE] func: {f.__name__}, args: {args}, kwargs: {kwargs}")
        return f(*args, **kwargs)
    return wrap

# Applying decorator to a function
@trace
def add_two(x):
    return x + 2

# Calling the decorated function
add_two(3)

# Applying decorator to a lambda
print((trace(lambda x: x ** 2))(3))

# It' useful for debugging purpose to apply a decorator to a lambda function,
# like below.
print(list(map(trace(lambda x: x*2), range(3))))


# In the functions below, the decorator function doesn't call the decorated
# function, so when the decorated function call is made for add_two(10),
# trace(10) is executed first and then the execution quits without executing the
# body of decorated function.
def decorator_trace(f):
    def trace(*args, **kwargs):
        print(f"{f.__name__} is being called with args {args} and kwargs {kwargs}")
    return trace

@decorator_trace
def add_two(x):
    print(x+2)
    return

add_two(10)      
