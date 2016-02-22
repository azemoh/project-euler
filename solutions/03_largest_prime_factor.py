# Problem 3 Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(num):
  """Returns the largest prime factor"""
  factor = 0
  div = 2
  while num > 1:
    if num % div == 0:
      factor = div
      num /= div
    div += 1

  return factor


def main():
  print largest_prime_factor(600851475143)


if __name__ == '__main__':
  main()
