with open("24_2508.txt") as f:
   a = f.readlines()

d = {}
for i in range(len(a)):
   c = a[i].count("Q")
   d[i] = c

maxi = max(d.values())
for i in d.keys():
   if d[i]==maxi:
      print(i)

j = 835
d={}
for i in a[j][:-1]:
   d[i] = d.setdefault(i,0)+1
mini=min(d.values())
for i in d.keys():
   if d[i]==mini:
      with open("24_2508.txt") as f:
         a = f.read()
      print(i,a.count(i))