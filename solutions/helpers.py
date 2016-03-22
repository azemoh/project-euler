# Helper methods

def sqrt(n):
  """
  Return the round down valule of the
  square root of integer n
  """
  return int(n ** (0.5))


def is_prime(n):
  """
  Test if a given integer is a prime number
  """
  if n < 2 or n % 2 == 0:
    return False
  elif n <= 3:
    return True

  for x in range(3, sqrt(n) + 1, 2):
    if n % x == 0:
      return False

  return True
