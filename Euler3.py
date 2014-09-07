def euler_three(num):

    if num < 0:
        print ("Error: negative number")
        return
    elif num < 2:
        return num
    
    prime_factor = 2
    while num > prime_factor:
        if num % prime_factor == 0:
            num = num / prime_factor    # divide out factors completely
        else:
            prime_factor += 1 # move to next factor after dividing out

    return prime_factor

# was originally part of code to produce next prime factor
# - taken out for efficiency
def next_prime(prev_prime):
    if prev_prime < 2:
        return 2

    next_prime = 3
    is_prime = True
    prime_list = [2]
    
    while next_prime <= prev_prime or is_prime == False:
        is_prime = True
        # checks if number in consideration is prime
        for prime in prime_list:
            # Iterates through all primes in list
            if next_prime % prime == 0:
                next_prime += 2
                is_prime = False
                break
        # if prime, add prime to list
        if is_prime == True:
            prime_list.append(next_prime)

    return next_prime
