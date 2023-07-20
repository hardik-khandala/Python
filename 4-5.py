def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False
    else:
        return True

def prime_numbers_up_to_N(n):
    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list

n = int(input("Enter a number: "))
primes = prime_numbers_up_to_N(n)
print(primes)