def euler_one(num):
    """
    - triangle numbers used to produce results in constant time
    - modified its formula Tn = n * (n + 1) / 2 for multiples of x
    => n = # of multiples of x
    => Tnx = x * n * (n + 1) / 2
    Proof at:
    http://jwilson.coe.uga.edu/EMT668/EMAT6680.F99/Jones/EMAT%206600/Problem%20Solving/Triangular%20Numbers/triangular.html
    """
    total = 0
    below_num = num - 1 # Asking for sum of natural numbers below given number
    
    tri = below_num // 3        # number of multiples of three in range
    quint = below_num // 5      # number of multiples of five in range
    fifteen = below_num // 15   # number of multiples of fifteen in range

    # Add all multiples of three to total
    if tri > 0:
        total = total + (3 * tri * (tri + 1) / 2)

    # Add all multiples of five to total
    # (Will double-count numbers that are also multiples of three)
    if quint > 0:
        total = total + (5 * quint * (quint + 1) / 2)

    # Subtract all multiples of fifteen from total
    # (Removes one set of the double-counted numbers that are both 3x and 5x)
    if fifteen > 0:
        total = total - (15 * fifteen * (fifteen + 1) / 2)

    return total
