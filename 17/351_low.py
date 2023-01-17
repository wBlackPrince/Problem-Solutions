from fnmatch import fnmatch
from functools import reduce

data = [int(x) for x in open("17t/17-346.txt") ]

count, pows = 0, []

for i in range(len(data)-2):
    a,b,c = data[i],data[i+1],data[i+2]
    mas = [int(i) for i in (str(a) + str(b) + str(c)) if int(i) % 2 == 0]
    pow = reduce(lambda x,y: x*y, mas, 1)

    if pow <= 2*10**9 and fnmatch(str(pow),"11*6*"):
        count += 1
        pows.append(pow)

print(count, max(pows))