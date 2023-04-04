with open("26_225.txt") as f:
   a = [int(i) for i in f.readlines()[1:]]

volume = 1000000
a = sorted(a,reverse = True)

count,elem = 0, []
for i in range(len(a)):
   if sum(elem) + a[i] <= volume:
      count += 1
      elem.append(a[i])
   else:
      continue

for i in a:
   if sum(a[:-1]) + i <= volume and sum[a][i] > i:
      sum[a][-1] = i

print(count, min(elem))
