def euler_five(top_num):

    if top_num < 1:
        print("Error - number too small")
        return
    elif top_num == 1:
        return 1

    pos_num = top_num * (top_num - 1)   # smallest evenly divisible unit possible
    even_divisor = False                # marks if evenly divisible

    base_unit = top_num * (top_num - 1) # only multiples of base divisible unit possible

    while even_divisor == False:
        for i in range(2, top_num):     # checks if number is divisble by range
            if pos_num % i != 0:
                even_divisor = False
                pos_num += base_unit    # next candidate number is multiple of base num
                break
            else:
                even_divisor = True

    return pos_num
