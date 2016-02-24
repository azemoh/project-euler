"""
Problem 6 Sum square difference
The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 - 385 = 2640. Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.
"""
def sum_squares(n):
  return sum([x**2 for x in range(1,n+1)])

def squared_sum(n):
  return sum([x for x in range(1,n+1)]) ** 2

def sum_square_difference(num):
  return squared_sum(num) - sum_squares(num)

def main():
  print sum_square_difference(100)


if __name__ == '__main__':
  main()
