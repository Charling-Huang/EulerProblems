def euler_six(n):

    """
    Sum of the first n numbers = n * (n + 1) / 2
    Sum of the first n square numbers = n * (n + 1) * (2n + 1) / 6
    Proof at:
    http://pirate.shu.edu/~wachsmut/ira/infinity/answers/sm_sq_cb.html
    """
    
    sq_total = n * (n + 1) * (2 * n + 1) / 6
    sum_total = pow(n * (n + 1) / 2, 2)

    return sum_total - sq_total
