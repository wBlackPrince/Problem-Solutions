from fnmatch import fnmatch

data = [int(x) for x in open("17t/17-346.txt") ]

def Pow(a,b,c):
    s = str(a) + str(b) + str(c)
    pow = 1
    for i in s:
        pow *= int(i)
    return pow

def Checker(a,b,c):
    pow = Pow(a,b,c)

    if pow <= 2*10**9 and fnmatch(str(pow),"83*8*"):
        return (True,pow)
    else:
        return (False,0)

count = 0
mas = []

for i in range(len(data)-2):
    result,pow = Checker(data[i],data[i+1],data[i+2])
    if result:
        count += 1
        mas.append(pow)

print(count, max(mas))

'''
def check_mask(num):
    if str(num)[:2] == "83" and  "3" in str(num)[2:]:
        return True
    else:
        return False
'''