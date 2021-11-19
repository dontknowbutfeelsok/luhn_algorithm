#credit card verifier
import random
import time


a = [int(i) for i in range(0,10)]
creditcardno = []

boolean = False

def isValidCredit(number):

    i = 1
    n = 0
    testarr_second_int = []
    c = []
    f = []    

    testarr = [int(x) for x in str(number)]

    while i != len(str(number)) or i != len(str(number)) + 1:
        try:
            testarr_second_int.append(testarr[i])
            i += 2
        except IndexError:
            break

    while n != len(str(number)) or n != len(str(number)) + 1:
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

    whole_sum = finstr_sum + cinstr_sum

    if whole_sum % 10 == 0:
        boolean = True
    else:
        boolean = False

while boolean == False:
    raw_i = 0
    while raw_i < 16:
        creditcardno.append(random.choices(a))    
        raw_i+=1
    #it creates a flatten list out of a list of lists
    creditcardno_flatlist = sum(creditcardno, [])

    #converts list to int
    creditcardno_real = int(''.join(map(str, creditcardno_flatlist)))

    print(creditcardno_real, '\n')

    time.sleep(0.2)

    isValidCredit(creditcardno_real)
