data = [int(x) for x in open("17t/17-346.txt") ]

def check_mask(num):
    if str(num)[:2] == "11" and  "6" in str(num)[2:]:
        return True
    else:
        return False

def Pow(a,b,c):
    s = str(a) + str(b) + str(c)
    pow = 1
    for i in s:
        if int(i)%2 == 0:
            pow *= int(i)
    return pow

count = 0
mas = []

for i in range(len(data)-2):
    pow = Pow(data[i],data[i+1],data[i+2])
    result = pow <= 2*10**9 and check_mask(pow)

    if result:
        count += 1
        mas.append(pow)

print(count, max(mas))
# 37 113246208