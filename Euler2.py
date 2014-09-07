def euler_two(upper_limit):

    # First two Fibonacci numbers
    fib_one = 1
    fib_two = 2
    
    total = 0

    # Iterative Fibonacci number generator with even-number ID
    while fib_two < upper_limit:
        if fib_two % 2 == 0:        # check if Fibonacci number is even
            total = total + fib_two # if Fibonacci number even, add to total
        temp = fib_one              # temporary variable to hold fib_one
        fib_one = fib_two           # assign value of fib_two to fib_one
        fib_two = temp + fib_two    # calculate next Fibonacci num, assign to fib_two

    return total
        
