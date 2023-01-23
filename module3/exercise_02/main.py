import random
import timeit

def fib(iters):
    i0 = 0
    i1 = 1
    i_n = i0 + i1
    for i in range(iters - 2):
        i0 = i1
        i1 = i_n
        i_n = i1 + i0
    
    return i_n

# Could not use the time module because the elapsed time kept resulting in 0.0
num = random.randint(15, 35)
result = timeit.timeit(stmt='fib(' + str(num) + ')', globals=globals(), number=1)

print('fib(' + str(num) + ')=' + str(fib(num)))
print('fib(' + str(num) + ') took ' + str(result) + ' seconds')