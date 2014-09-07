def euler_nine(num):
    
    # Brute force correct a and b
    a = num
    b = num
    c = 0

    # Check if agrees with constraints and that no variables == 0
    while a + b + c != num or pow(a, 2) + pow(b, 2) != pow(c, 2) or a == 0 or c == 0:
        if a < 1:           # if a < 1 then decrement b
            b -= 1
            a = num - b     # start a over at max num it can be
        else:
            a -= 1          # decrement a normally
        c = pow(pow(a, 2) + pow(b, 2), 0.5) # calculating c

        if b == 0:
            print("Error: No valid combination") # if b reaches 0, all a/b combos have been tried; exit
            return
        
    return a * b * c
