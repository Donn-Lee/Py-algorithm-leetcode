def fibonacci(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
import timeit
#print(print(timeit.timeit('fibonacci(140)', globals=globals(), number=1000)))

memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        return 0 
    elif n == 1:
        return 1
    result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = result
    return result
import time
start = time.clock()

print(fibonacci_memo(30))
end = time.clock()
print(str(end-start))


start = time.clock()

print(fibonacci(30))
end = time.clock()
print(str(end-start))