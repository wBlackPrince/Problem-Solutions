with open("22_6.txt") as f:
    a = f.readlines()
    for i in range(len(a)):
        a[i] = a[i].replace(";","\t")
    a = [i.split("\t") for i in a]

d = {}
for i in a:
    d[int(i[0])] = [int(i) for i in i[1:]]

def time(id):
    global d

    if d[id][1] == 0:
        return d[id][0]
    return max([time(i) for i in d[id][1:]]) + d[id][0]

print(max([i[0] for i in d.values()]))   # 1000 если все процессы параллельны

mas = []
for i in d.keys():
    mas.append(time(i)) 
print(max(mas))             #20288 с последовательными процессами

# Ответ = 20288-1000= 19288
