import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def show_primes(lst):
    print("Prime numbers:")
    for n in lst:
        if is_prime(n):
            print(n, end=" ")
    print()

def show_nonprimes(lst):
    print("Non-prime numbers:")
    for n in lst:
        if not is_prime(n):
            print(n, end=" ")
    print()

lst = [10, 3, 5, 8, 11, 15, 7, 9]

t1 = threading.Thread(target=show_primes, args=(lst,), name="Prime")
t2 = threading.Thread(target=show_nonprimes, args=(lst,), name="NonPrime")

t1.start()
t2.start()

t1.join()
t2.join()
