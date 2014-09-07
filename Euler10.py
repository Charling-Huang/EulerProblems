def euler_ten(limit):

    """
    prime num generator using Sieve of Eratosthenes
    found at:
    http://pythonism.wordpress.com/2008/05/04/looking-at-prime-numbers-in-python/
    
    # Generate list of primes under given limit
    a=list(range(2,limit))
    for x in a:
        comp=[]
        for y in range(a.index(x),len(a)):
            q=x*a[y]
            if q<=max(a):
                comp.append(q)
            else:
                break
        for z in comp:
            a.remove(z)
    
    return sum(a)
    """

    if limit <= 1:
        return 0
    elif limit < 3:
        return 2

    next_prime = 3
    prime_list = [2]
    
    while next_prime < limit:
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
    
    return sum(prime_list)   
