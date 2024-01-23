"""
This will be a recursion playground for me. Just testing some fun stuff out

Author: Ryley Turner
"""

def find_fact(n):
	if n == 1:
		return n
	else:
		return find_fact(n - 1) * n
		

print(find_fact(int(input("What would you like to find the factorial of?: "))))