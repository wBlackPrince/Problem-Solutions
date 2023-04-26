with open("2.txt") as f:
   a = [[int(j) for j in i.split("\t")]for i in f.readlines()]

def checker(a,b,c,d):
   if a==b==c==d: return 0
   return (a==c and b==d)

c=0
for i in a:
   if checker(i[0],i[1],i[2],i[3]):
      c+=1
print(c)