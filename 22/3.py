with open("22_3.txt") as f:
    a = f.readlines()
    for i in range(len(a)):
        a[i] = a[i].replace("; ","\t")[:-1].split('\t')

dicti = {}
for i in a:
    dicti[int(i[0])] = [int(i) for i in i[1:]]


def time(n):
    if dicti[n][1] == 0: return dicti[n][0]
    return max([time(i) for i in dicti[n][1:]]) + dicti[n][0]

mas = []
for i in dicti:
    mas.append(time(i))
print(mas)