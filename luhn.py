#credit card verifier

#from random import randint
#import re

i = 1
b = []
c = []
d = []

#a = [int(i) for i in range(0,10)]

test = 79927398713

testarr = [int(x) for x in str(test)]


while i != len(str(test)) or i != len(str(test)) + 1:
    try:
        b.append(testarr[i])
        i += 2
    except IndexError:
        break
    
for i in b:
    c.append(i*2)
    i+=1

for w in c:
    if len(c[w]) > 0:
        d.append(c[w])
        print(d)
        w+=1

print('c =', c)



    

