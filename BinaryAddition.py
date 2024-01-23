"""
I want to mess around with binary addition, this is my place of doing that

Author: Ryley Turner
"""

SIZE = 8  # Allows for arbitrarily long binary sequences.
BINARY_SIZE = SIZE - 1

def main():
    A = convert_int_to_binary(int(input("Enter Integer A: ")))
    B = convert_int_to_binary(int(input("Enter Integer B: ")))
    print(f"A = {A}\nB = {B}")
    print(f"A + B = {add_binary_strings(A, B)} or {convert_binary_to_int(add_binary_strings(A, B))}")


def convert_int_to_binary(number):
    binary_string = ""

    for i in range(BINARY_SIZE, -1, -1):
        if number >= 2 ** i:
            binary_string += "1"
            number -= 2 ** i
        else:
            binary_string += "0"

    return binary_string


def add_binary_strings(string1, string2):
    final_string = ""
    carry = 0
    string1 = string1[::-1]
    string2 = string2[::-1]

    for i in range(len(string1)):
        if string1[i] == "1" and string2[i] == "1":
            if carry > 0:
                final_string += "1"
            else:
                carry += 1
                final_string += "0"
        elif string1[i] != string2[i]:
            if carry > 0:
                final_string += "0"
            else:
                final_string += "1"
        else:
            if carry > 0:
                carry -= 1
                final_string += "1"
            else:
                final_string += "0"

    return final_string[::-1]


def convert_binary_to_int(binary_string):
    total = 0

    for i in range(1, len(binary_string) + 1):
        if binary_string[-i] == "1":
            total += 2 ** (i - 1)

    return total


if __name__ == "__main__":
    main()