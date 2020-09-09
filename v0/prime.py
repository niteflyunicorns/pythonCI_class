def is_prime(number): 
	if (number <= 1):
		return False

	if (not type(number) is int):
		return False

	for element in range(2,number): 
		if (number % element == 0):
			return False
	return True 
