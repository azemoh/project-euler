# Problem 4 Largest palindrome product
# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product():
  largest = 0
  for x in range(100, 1000):
    for y in range(100, 1000):
      num = x * y
      len_n = len(str(num))
      if len_n % 2 == 0:
        if str(num)[:len_n/2] == str(num)[len_n/2:][::-1]:
          if num > largest: largest = num

  return largest

def main():
  print largest_palindrome_product()


if __name__ == '__main__':
  main()
