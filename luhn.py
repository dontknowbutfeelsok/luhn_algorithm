#credit card cinstr_sumerifier

i = 1
testarr_second_int = []
c = []

#a = [int(i) for i in range(0,10)]

test = 79927398713

testarr = [int(x) for x in str(test)]

while i != len(str(test)) or i != len(str(test)) + 1:
    try:
        testarr_second_int.append(testarr[i])
        i += 2
    except IndexError:
        break
    
for i in testarr_second_int:
    c.append(i*2)
    i+=1

cinstr = ''.join(map(str, c))

cinstr_sum = sum(map(int, cinstr))

m = [k for k in testarr if k not in c]

minstr = ''.join(map(str, m))

minstr_sum = sum(map(int, minstr))


print('c =', c)
print('cinstr =', cinstr)
print('cinstr_sum =', cinstr_sum)
print('type of cinstr =', type(cinstr))

print('''
=================================

=================================

=================================
''')

print('testarr =', testarr)
print('      m =', m)
print('testarr_second_int =', testarr_second_int)

print(minstr_sum + cinstr_sum)

