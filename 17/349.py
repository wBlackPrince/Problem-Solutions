from fnmatch import fnmatch

data = [int(x) for x in open("17t/17-346.txt") ]

def Pow_Triple(a,b,c):
    p = 1
    for i in (str(a) + str(b) + str(c)):
        p *= int(i)
    return p

def pow_nums(a,b,c):
    p = Pow_Triple(a,b,c)
    if p < 2_000_000_000 and fnmatch(str(p),'83*8*'):
        return (True,p)
    else:
        return (False,0)

array = []
count = 0

for i in range(len(data)-2):
    flag,result = pow_nums(data[i],data[i+1],data[i+2])
    if flag:
        array.append(result)
        count += 1


print("наибольшее произведение цифр", max(array),"количество троек", count)
# 839808000 3