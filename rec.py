def rec_sum(array,i = 0,sum = 0):
    if i == len(array):
        return sum
    else:
        sum += array[i]
        return rec_sum(array,i+1,sum)


n = 1
def fib(a = 1,b = 0, const = 1):
    if const == n:
        return a
    else:
        return fib(a = a+b, b = a, const = const + 1)

print(fib())