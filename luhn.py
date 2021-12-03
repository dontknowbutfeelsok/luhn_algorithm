#credit card verifier/generator
from random import choices
from time import sleep
import isValid

a = [int(i) for i in range(0,10)]
creditcardno = []

while True:

    creditcardno.clear()
    
    raw_i = 0
    while raw_i < 16:
        creditcardno.append(choices(a))    
        raw_i+=1

    #it creates a flatten list out of a list of lists
    creditcardno_flatlist = sum(creditcardno, [])

    #converts list to str
    creditcard = ''.join(map(str, creditcardno_flatlist))

    print('checking', int(creditcard))

    if isValid.isValidCredit(creditcard) == True:
        print('Your credit card numbers is valid.\n')
        break
    else:
        print('No. is Invalid.\n')
        sleep(0.1)
        continue
