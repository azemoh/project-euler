# Problem 5 Smallest Multiple
# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple():
  i = 2
  multiple = 0
  while True:
    multiple = 20 * i
    if all(multiple % n == 0 for n in range(1,21)): break
    i += 1
  return multiple

def main():
  print smallest_multiple();


if __name__ == '__main__':
  main()
