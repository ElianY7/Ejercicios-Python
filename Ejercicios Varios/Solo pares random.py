from random import randint

lis = [randint(1,100) for i in range(10)]

print (lis) 

par = [ ] 

for i in lis:
  
    if i % 2 == 0:
        par.append(i)


print(par)
