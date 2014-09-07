from Euler7a import euler_seven
import time

# timeit.timeit('from Euler1 import euler_one; euler_one(num)',setup='num=10' )

start = time.time()
print euler_seven(100)
print time.time() - start

