with open("d10.txt", "r") as f:
   a = [i.replace(";","\t") for i in f.readlines()]
a = [i[:-1].split("\t") for i in a]

d = {}
for i in a:
   d[int(i[0])] = [int(j) for j in i[1:]]

print(d)

def time(n):
   if d[n][1] == 0: return d[n][0]
   return max(time(i) for i in d[n][1:]) + d[n][0]

def main(id):
   mas = []
   d[16][1] = id

   for i in d.keys():
      mas.append(time(i))

   return max(mas)

for t in range(1,21):
   if main(t) == 138:
      print(t)
      break