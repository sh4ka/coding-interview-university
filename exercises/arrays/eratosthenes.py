def primes(n):
    n = int(n[0])
    is_prime = [True] * (n + 1)
    div = 2
    while (div * div) <= n:
        if is_prime[div]:
            i = 2 * div
            while i <= n:
                is_prime[i] = False
                i += div
        div += 1
                
    for i in range(0, len(is_prime)):
        if is_prime[i]:
            print('{} is prime'.format(i))
    

if __name__ == '__main__':
    import sys
    primes(sys.argv[1:])