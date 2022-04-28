import random
if __name__ == "__main__":
  board = input()
  x = random.randint(1, 8)
  y = random.randint(1, 8)
  while(y%2 != x%2):
    y = random.randint(1, 8)
  z = random.randint(0, 1)
  a = ""
  a += str(x) + " "
  a += str(y) + " "
  a += str(x+[[-1, 1], [-2, 2]][z][random.randint(0, 1)]) + " "
  a += str(y+[[-1, 1], [-2, 2]][z][random.randint(0, 1)])
  print(a)