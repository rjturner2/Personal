"""
This script will add all add increasing orders of odd integers together and tell me if they
are perfect squares or not

Author: (Ryley Turner)
"""

from math import sqrt


def sum_odd_integers(limit):
    summation = 0

    for i in range(limit):
        summation += (2 * i + 1)

    return summation


def main():
    for i in range(1000000):
        print(sum_odd_integers(i))


if __name__ == "__main__":
    main()
