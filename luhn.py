#credit card cinstr_sumerifier

i = 1
n = 0
testarr_second_int = []
c = []
f = []

#a = [int(i) for i in range(0,10)]

test = 7992738713

testarr = [int(x) for x in str(test)]

while i != len(str(test)) or i != len(str(test)) + 1:
    try:
        testarr_second_int.append(testarr[i])
        i += 2
    except IndexError:
        break
while n != len(str(test)) or n != len(str(test)) + 1:
    try:
        f.append(testarr[n])
        n += 2
    except IndexError:
        break
    
for i in testarr_second_int:
    c.append(i*2)
    i+=1

#c to str and then sum

cinstr = ''.join(map(str, c))

cinstr_sum = sum(map(int, cinstr))

#m = [k for k in testarr if k not in testarr_second_int]

#f to str and then sum

finstr = ''.join(map(str, f))

finstr_sum = sum(map(int, finstr))

print('finstr_sum + cinstr_sum =', finstr_sum + cinstr_sum)

def isValidCredit():
    if (finstr_sum + cinstr_sum) % 10 == 0:
        print('Yes')
    else:
        print('No')


isValidCredit()

