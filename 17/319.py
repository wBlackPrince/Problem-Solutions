data = [int(i) for i in open("17t/17-316.txt")]

sred_arif = sum(data)/len(data)

def CheckCond(a,b):
    return (a//1000 + b//1000) == (a%10 + b%10)

def F(a,b,c):
    return (CheckCond(a,b) or CheckCond(b,c) or CheckCond(a,c)) and (a+b+c)/3 > sred_arif

count = 0
summs_triple = []

for i in range(len(data)-2):
    a,b,c = data[i],data[i+1],data[i+2]

    if F(a,b,c):
        count += 1
        summs_triple.append(a+b+c)

print(count, max(summs_triple))

#877 28668