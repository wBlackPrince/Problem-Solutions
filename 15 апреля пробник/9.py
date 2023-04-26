with open("9.txt") as f:
   a = [[int(j) for j in i[:-1].split("\t")] for i in f.readlines()]

def checker(a,b,c,d):
   return any([a ==b and c == d, 
               a == c and b == d,
               a == d and c == b])

c = 0
for i in a:
   if checker(i[0],i[1],i[2],i[3]):
      c+=1
print(c)