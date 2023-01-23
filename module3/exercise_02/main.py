import random
import time

def fib(iters):
    i0 = 0
    i1 = 1
    i_n = i0 + i1
    for i in range(iters - 2):
        i0 = i1
        i1 = i_n
        i_n = i1 + i0
    
    return i_n

start = time.time() * 10 ** 6
num = random.randint(15, 35)
end = time.time() * 10 ** 6

print('fib(' + str(num) + ')=' + str(fib(num)))
print('fib(' + str(num) + ') took ' + str(end - start) + ' seconds')