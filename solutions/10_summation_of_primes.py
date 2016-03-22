"""
Problem 10 Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

NUMBER = 2000000


def sqrt(n):
  """
  Return the round down valule of the
  square root of integer n
  """
  return int(n ** (0.5))

def is_prime(n):
  if n < 2 or n % 2 == 0:
    return False
  elif n <= 3:
    return True

  for x in range(3, sqrt(n) + 1, 2):
    if n % x == 0:
      return False

  return True

def main():
  filtered = [i for i in range(3, NUMBER, 2)]
  print (2 + sum(i for i in filtered if is_prime(i)))


if __name__ == '__main__':
  main()
