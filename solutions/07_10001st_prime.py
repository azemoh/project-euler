"""
Problem 7 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10001st prime number? 104743
"""

from helpers import is_prime


def nth_prime(n):
  num = 1
  prime = 1
  prime_count = 0
  while prime_count <= n:
    if is_prime(num):
      prime = num
      prime_count += 1
    num += 2

  return prime


def main():
  print nth_prime(10001)


if __name__ == '__main__':
  main()
