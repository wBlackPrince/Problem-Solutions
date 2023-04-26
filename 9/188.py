with open("188.txt") as f:
   a = [[int(j) for j in i.split("\t")] for i in f.readlines()]

def checker(a,b,c):
   bools = [(a*b)%10 == 4, (a*c)%10 == 4, (b*c)%10 == 4]
   return any(bools)

c = 0
for i in a:
   if checker(i[0], i[1], i[2]):
      c+=1
print(c)

#965