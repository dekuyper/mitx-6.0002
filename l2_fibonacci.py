def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fast_fib(n: int, memo={}):
    '''Dynamically computes the Fibonacci of "n"'''
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fast_fib(n - 1, memo) + fast_fib(n - 2, memo)
        memo[n] = result

        return result


def test_fast_fib():
    for n in range(121):
        print('fib({0}) = {1}'.format(n, fast_fib(n)))


def test_fib():
    for n in range(121):
        print('fib({0}) = {1}'.format(n, fib(n)))


test_fast_fib()

