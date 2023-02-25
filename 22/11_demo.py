with open("d11.txt", "r") as f:
   a = [i.replace(";","\t") for i in f.readlines()]
a = [i[:-1].split("\t") for i in a]

d = {}
for i in a:
   d[int(i[0])] = [int(j) for j in i[1:]]

print(d)

def time(n,c=0):
   if c> 200: return 0
   if d[n][1] == 0: return d[n][0]
   return max(time(i,c+1) for i in d[n][1:]) + d[n][0]

def main(id):
   mas = []
   d[12][1] = id

   for i in d.keys():
      mas.append(time(i))

   return max(mas)

for t in range(1,21):
   if main(t) == 154:
      print(t)
      break