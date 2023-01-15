data = [int(i) for i in open("17t/17-328.txt")]

max_element = max([int(i) for i in data if int(i)%50 == 0])

def check_palin(a,b):
    return (str(a+b) == str(a+b)[::-1],a+b)

def checker(a,b,c):
    p1,p2,p3 = check_palin(a,b),check_palin(a,c),check_palin(b,c)
    return (p1[0] and p2[0] and p3[0]) and max(p1[1],p2[1],p3[1]) < max_element

count = 0
array = []

for i in range(len(data)-2):
    a,b,c = data[i],data[i+1],data[i+2]
    if checker(a,b,c):
        count += 1
        array.append(a+b+c)

print(count, max(array))
# 96 13398