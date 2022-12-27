def reader(file_name):
    with open(file_name) as f:
        a = f.readlines()
        for i in range(len(a)):
            a[i] = a[i].replace("; ","\t")
        a = [i.split("\t") for i in a]

    d = {}
    for i in a:
        d[int(i[0])] = [int(i) for i in i[1:]]
    return d

def time(id,d):
    if d[id][1] == 0:
        return d[id][0]
    return max([time(i,d) for i in d[id][1:]]) + d[id][0]

d1 = reader("22_5_1.txt")
d2 = reader("22_5_2.txt")

mas = []
for i in d1.keys():
    mas.append(time(i,d1))
print(max(mas))

mas = []
for i in d2.keys():
    mas.append(time(i,d2))
print(max(mas))

# ответ 1