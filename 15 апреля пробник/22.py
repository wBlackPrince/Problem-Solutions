with open("22.txt") as f:
   a = f.read().replace(";", "\t").split("\n")[:-1]
   a = [i.split("\t") for i in a]

d = {}
for i in a:
   d[(int(i[0]))] = [int(j) for j in i[1:]]

def time(n):
   global d
   
   if d[n][1] == 0: return d[n][0]
   return max([time(i) for i in d[n][1:]]) + d[n][0]


mas = []
for i in d.keys():
   mas.append(time(i))

print(max(mas))