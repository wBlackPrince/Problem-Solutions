with open("5.txt") as f:
   a = [[int(j) for j in i.split("\t")]for i in f.readlines()]

def checker(a,b,c):
   return (a+b+c == 180) and (a==b or a==c or b==c)

c=0
k = 0
for i in a:
   if checker(i[0],i[1],i[2]):
      c+=1
   if sum([i[0],i[1],i[2]]) == 180:
      k+=1

print(c/k*100)