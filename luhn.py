#credit card verifier/generator
import random
import time
import isValid

a = [int(i) for i in range(0,10)]
creditcardno = []

while isValid.boolean == False:
    raw_i = 0
    while raw_i < 16:
        creditcardno.append(random.choices(a))    
        raw_i+=1
    if len(creditcardno) > 16:
        creditcardno.clear()
    #it creates a flatten list out of a list of lists
    creditcardno_flatlist = sum(creditcardno, [])

    #converts list to int
    creditcard = ''.join(map(str, creditcardno_flatlist))

    creditcard.strip()

    print(creditcardno_flatlist)

    print('checking ', creditcard, '\n')

    time.sleep(0.2)

    isValidCredit(int(creditcard))
