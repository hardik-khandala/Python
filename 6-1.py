def find_primes(start, end): 
	primes = [] 
	for num in range(start, end + 1): 
		if num > 1: 
			for i in range(2, int(num**0.5) + 1): 
				if (num % i == 0): 
					break
			else: 
				primes.append(num) 
	return primes

# Print the prime numbers in the range 1 to 100
print(list(filter(lambda x: x > 10, find_primes(1, 30))))
