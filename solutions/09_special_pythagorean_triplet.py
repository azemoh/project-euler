"""
Problem 9 Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

NUMBER = 1000

def is_py_triplet(a,b,c):
  return a * a + b * b == c * c

def product():
  for a in range(1, NUMBER + 1):
    for b in range(1, NUMBER + 1):
      c = NUMBER - (a + b)
      if is_py_triplet(a, b, c):
        return a * b * c

def main():
  print product()


if __name__ == '__main__':
  main()
