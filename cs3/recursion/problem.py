# Calculate the factorial of `n` recursively

def factorial(n):
	if n == 0:
		return 1

	return n * factorial(n - 1)

print(factorial(10)) # Should print 3628800

# Calculate the nth fibonacci number recursively
#
# fibonacci(10) should return 55

def fibonacci(n):
	# Your code goes here
	pass

print(fibonacci(10)) # Should print 55

# Calculate the `2 ** n` recursively, without using the
# built-in exponentiation functionality

def power2(n):
	# Your code goes here
	pass

print(power2(10)) # Should print 1024

# Calculate the sum of the numbers in a list recursively

def total(numbers, index):
	# Your code goes here
	pass

print(total([1, 2, 3, 4, 5], 0)) # Should print 15

# Check if a list of items contains a value recursively

def contains(items, value, index):
	# Your code goes here
	pass

print(contains(["a", "s", "d", "f"], "d", 0)) # Should print True
