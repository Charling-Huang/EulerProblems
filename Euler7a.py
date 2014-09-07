def euler_seven(nth):

    # Brute-force way to get nth prime number

    if nth <= 1:
        return 2

    nth_prime = 3
    prime_list = [2]
    prime_string = ""
 
    while len(prime_list) < nth:
        is_prime = True
        # checks if number in consideration is prime
        for prime in prime_list:
            # Iterates through entire list of primes so far
            if nth_prime % prime == 0:
                nth_prime += 2
                is_prime = False
                break
        # if prime, add to list of primes
        if is_prime == True:
            prime_list.append(nth_prime)
   	    prime_string = prime_string + ":" + str(nth_prime)
 
    return nth_prime,prime_string   
