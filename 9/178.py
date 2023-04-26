with open("178.txt") as f:
   a = [[int(j) for j in i.split("\t")] for i in f.readlines()]

s = [i**3 for i in range(1,1000)]

def checker(mas):
   p1 = mas[0]*mas[1]
   p2 = mas[0]*mas[2]
   p3 = mas[1]*mas[2]
   return len(mas) == len(set(mas)) and any([p1 in s, p2 in s, p3 in s])

c= 0
for i in a:
   if checker(i):
      c+=1
print(c)
#53