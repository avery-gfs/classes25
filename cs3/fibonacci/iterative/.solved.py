# Calculate the nth fibonacci number
#
# fibonacci(10) should return 55

def fibonacci(n):
	seq = [0, 1]

	for i in range(n - 1):
		seq.append(seq[-1] + seq[-2])

	return seq[n]

print(fibonacci(10))
