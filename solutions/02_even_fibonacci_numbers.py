# Problem 2 Even fibonacci numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


#  Bottom-up algorithm with memoization
def fibonacci(n):
  memo = [1,1]

  if n > 2:
    for x in range(3,n+1):
      f = memo[1] + memo[0]
      memo[0] = memo[1]
      memo[1] = f

  return memo[1]


def main():
  even_sum = 0
  num = 1
  fib = 0
  while fib < 4000000:
    fib = fibonacci(num)

    if fib % 2 == 0:
      even_sum += fib
    num += 1

  print even_sum


if __name__ == '__main__':
  main()
