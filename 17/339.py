data = [int(i) for i in open("17t/17-339.txt")]

min_el = min([int(i) for i in data if int(i) > 0 and int(i)%19 == 0])

def checker(a,b):
    return (a+b) < min_el

count, array = 0, []

for i in range(len(data)-2):
    if checker(data[i],data[i+1]):
        count += 1
        array.append(data[i] + data[i+1])

print(count, abs(max(array)))
# 4984 696