"""
Problem 7 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10001st prime number? 104743
"""

def is_prime(n):
  if n < 2: return False
  return all(n % x != 0 for x in range(2,int(n/2)))

def nth_prime(n):
  num = 1
  prime = 2
  count = 0
  while count <= n:
    if is_prime(num):
      prime = num
      count += 1
    num += 1

  return prime


def main():
  print nth_prime(10001)


if __name__ == '__main__':
  main()

