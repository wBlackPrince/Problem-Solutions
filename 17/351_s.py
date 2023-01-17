from fnmatch import fnmatch
from functools import reduce

data = [int(x) for x in open("17t/17-346.txt") ]

def Pow(a,b,c):
    mas = [int(i) for i in (str(a) + str(b) + str(c)) if int(i) % 2 == 0]
    return reduce(lambda x,y: x*y, mas, 1)

def Checker(a,b,c):
    pow = Pow(a,b,c)

    if pow <= 2*10**9 and fnmatch(str(pow),"11*6*"):
        return (True,pow)
    else:
        return (False,0)

count,mas = 0, []

for i in range(len(data)-2):
    result,pow = Checker(data[i],data[i+1],data[i+2])
    if result:
        count += 1
        mas.append(pow)


print(count, max(mas))
# 37 113246208
