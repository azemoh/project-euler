"""
Problem 10 Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

from helpers import is_prime


NUMBER = 2000000


def main():
  filtered = [i for i in range(3, NUMBER, 2)]
  print (2 + sum(i for i in filtered if is_prime(i)))


if __name__ == '__main__':
  main()
