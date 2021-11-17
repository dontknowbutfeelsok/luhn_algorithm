#credit card verifier

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

'''
first, you bring all the >1   numbers in one list by the while loop.
then you convert the list to a string by ''.join(map()) func{say y}; also
make a list of the left numbers {say g} in the variable c. then separate
every thing from y and create a list of that. then g + y. done. good job. 
'''

cisstr = ''.join(map(str, c))

print(cisstr)

w = 0

while w < len(cisstr):
    if len(''.join(map(str, c[w]))):
        d.append(c[w])
        print(d)
        w+=1
    else:
        continue

#print('c =', c)
#print('d =', d)
