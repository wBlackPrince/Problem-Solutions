

a = [300,350,400,1000,1500,2000]
lowest = sorted([i for i in a if i < 500])
biggest = sorted([i for i in a if i > 500])
disc_d_vol = 3000
disc_e_vol = 1000

def f(disc_e_vol,lowest,mas_e = []):
   for i in lowest:
      if sum(mas_e) + i <= disc_e_vol:
         mas_e.append(i)
      else:
         continue

   for i in lowest:
      if sum(mas_e[:-1]) + i <= disc_e_vol and mas_e[-1] < i:
         mas_e[-1] = i
   return mas_e  


mas_e =f (disc_e_vol, lowest)
mas_d =f (disc_d_vol, biggest)
count = len(mas_e) + len(mas_d)
maxi = max(mas_d) + max(mas_e)
print(count, maxi)
