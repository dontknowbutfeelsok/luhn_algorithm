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
