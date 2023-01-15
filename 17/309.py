data = [int(i) for i in open("17t/17-304.txt")]

min_el = min([i for i in data if i%54 == 0])

def checker(a):
    evaul_sum = sum([int(i) for i in (a) if int(i)%2 == 0])
    notevaul_sum = sum([int(i) for i in (a) if int(i)%2 != 0])
    return evaul_sum > notevaul_sum

def f(a,b):
    global min_el

    cond1 = checker(a) and checker(b)
    cond2 = (int(a) + int(b)) % min_el != 0

    return cond1 and cond2

c = 0
summs_el = []

for i in range(len(data)-1):
    if f(str(data[i]), str(data[i+1])):
        c += 1
        summs_el.append(data[i] + data[i+1])

print(c, min(summs_el))
# ответ 2096 1466
