with open("22_32.txt") as f:
    a = f.readlines()
    for i in range(len(a)):
        a[i] = a[i].replace(";","\t")
    a = [a[i].split("\t") for i in range(len(a)) if i != 15]

d = {}
for i in a:
    d[int(i[0])] = [int(i) for i in i[1:]]


def time(id):
    global d

    if d[id][1] == 0:
        return d[id][0]
    return max([time(i) for i in d[id][1:]]) + d[id][0]

for t in range(1,100):
    mas = []
    d[16] = [t,0]

    for i in d.keys():
        mas.append(time(i))
    
    if(max(mas)) == 134:
        print(t)
        break

# ответ 26