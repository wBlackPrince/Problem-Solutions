with open("24_2507.txt") as f:
   a = f.readlines()

def counter(s):
   maxi = 0
   letter = ""
   c = 1
   for i in range(len(s)-1):
      if s[i] == s[i+1]:
         c+=1
      else:
         if maxi < c:
            maxi = c
            letter = s[i]
         c=1
   if maxi < c:
      maxi = c
      letter = s[i]
   return maxi,letter

# частота
d = {}
# буквы
d1 = {}
for i in range(len(a)):
   d[i] = counter(a[i])[0]
for i in range(len(a)):
   d1[i] = counter(a[i])[1]

#161 765

'''maxi = max(d.values())
for i in d.keys():
   if d[i] == maxi:
      print(i)'''

d={}
for i in a[161]:
   d[i] = d.setdefault(i,0)+1

maxi = max(d.values())
for i in d.keys():
   if d[i] == maxi:
      with open("24_2507.txt") as f:
         a = f.read()
      print(i,a.count(i))