with open("d8.txt", "r") as f:
   a = [i.replace(";","\t") for i in f.readlines()]
a = [i[:-1].split("\t") for i in a]

d = {}
for i in a:
   d[int(i[0])] = [int(j) for j in i[1:]]

print(d)

def time(n):
   if d[n][1] == 0: return d[n][0]
   return max(time(i) for i in d[n][1:]) + d[n][0]

def main(t):
   mas = []
   d[3][0] = t

   for i in d.keys():
      mas.append(time(i))

   return max(mas)

for t in range(1,50):
   if main(t) > 107:
      print(t-1)
      break