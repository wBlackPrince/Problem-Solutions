with open("3.txt") as f:
   a = [[int(j) for j in i.split("\t")]for i in f.readlines()]

def checker(a,b,c):
   return (a==b and a!= c) or (b==c and b!=a) or (a==c and a!=b)

c=0
for i in a:
   if checker(i[0],i[1],i[2]):
      c+=1
print(c)