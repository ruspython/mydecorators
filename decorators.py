def benchmark_once(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.clock()
        res = func(*args, **kwargs)
        end = time.clock()
        print(func.__name__, ':', end-start)
        return res
    return wrapper

class benchmark_more(object):
    def __init__(self, times = 1000):
        self.times = times
    def __call__(self, original_func):
        import time
        decorator_self = self
        def wrapper( *args, **kwargs):
            start = time.clock()
            for x in range(decorator_self.times):
                res = original_func(*args, **kwargs)
            end = time.clock()
            print('<The fucntion %s was executed %d times in %f seconds>'%(
                original_func.__name__,
                decorator_self.times,
                end-start))
            return res
        return wrapper

def debugger(func):
    def wrapper(*args, **kwargs):
        print('Entering function:', func.__name__)
        res = func(*args, **kwargs)
        print('Result of', func.__name__, 'is', res)
        print('Finishing function:', func.__name__)
        return res
    return wrapper

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.execNumber += 1
        res = func(*args, **kwargs)
        print('The function', func.__name__, 'was executed', wrapper.execNumber, 'time' if wrapper.execNumber == 1 else 'times')
        return res
    wrapper.execNumber = 0
    return wrapper

if __name__ == '__main__':
    def reverse_this(string):
        return ''.join(reversed(string))

    @full_analys
    def reverse_that(string):
        return string[::-1]

    print(reverse_this('This is too many words text'))
    print(reverse_that('This is too many words text'))
    print(reverse_that('This is too many words text'))
    print(reverse_that('This is too many words text'))
    print(reverse_that('This is too many words text'))


