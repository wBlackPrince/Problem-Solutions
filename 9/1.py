with open("1.txt") as f:
   a = [[int(j) for j in i.split("\t")]for i in f.readlines()]

# проверка троек на ариф. прогрессию
def checker(a,b,c):
   return (a-b == b-c != 0) or (a-c == c-b!=0) or (b-a==a-c!=0) or (b-c==c-a!=0) or (c-a==a-b!=0) or (c-b==b-a!=0)

c=0
for i in a:
   if checker(i[0],i[1],i[2]):
      c+=1
print(c)