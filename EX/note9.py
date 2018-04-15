# Python高级编程技巧实战
# 2018/04/15

"""----------------------------"""

#裝式器
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def climb(n,steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step,steps)
    return count


# 增加緩存功能
def fibonacci(n,cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return 1
    cache[n] = fibonacci(n-1,cache) + fibonacci(n-2,cache)
    return cache[n]

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


@memo
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

@memo
def climb(n,steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step,steps)
    return count
    
"""----------------------------"""
def mydecorator(func):
    def wrapper(*args,**kargs):
        '''wrapper function'''
        print("in wraapre")
        func(*args,**kargs)
    wrapper.__name__ = func.__name__
    return wrapper


@mydecorator
def example():
    print('in example')

def example2():
    print('in example')


print(example.__name__)
print(example.__doc__)

print(example2.__name__)
print(example2.__doc__)


"""----------------------------"""
from functools import update_wrapper,wraps,WRAPPER_ASSIGNMENTS,WRAPPER_UPDATES

def mydecorator(func):
    # @wraps
    def wrapper(*args,**kargs):
        '''wrapper function'''
        print("in wraapre")
        func(*args,**kargs)
    # update_wrapper(wrapper,func,('__name__','__doc__'),('__dict__',))
    # update_wrapper(wrapper,func)
    return wrapper


@mydecorator
def example():
    print('in example')


print(example.__name__)
print(example.__doc__)


#默認參數
print(WRAPPER_ASSIGNMENTS)
print(WRAPPER_UPDATES)



