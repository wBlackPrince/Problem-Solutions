with open("22_46.txt") as f:
    a = f.readlines()
    for i in range(len(a)):
        a[i] = a[i].replace("; ","\t")
    a = [i.split("\t") for i in a]

d = {}
for i in a:
    d[int(i[0])] = [int(i) for i in i[1:]]

parallel_process = [i for i in d.keys() if d[i][1]==0]

print(parallel_process)