with open("4.txt") as f:
   a = [[int(j) for j in i.split("\t")]for i in f.readlines()]

print(a)
c = 0
for i in a:
   if ( i[0] + i[1] + i[2] )== 180:
      c+=1
print(c)