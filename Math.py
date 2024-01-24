summation = 0

def main():
	i = 0

	while left_sum(i) == right_sum(i):
		print(f"Case {i} Passed Successfully.")
		i += 1

	print(f"Case {i} Failed to Validate.")
	print(left_sum(i), right_sum(i))


def left_sum(i):
	global summation
	summation += i ** 2
	return float(summation)


def right_sum(i):
	return (i * (i + 1) * (2 * i + 1)) / 6


if __name__ == "__main__":
	main()