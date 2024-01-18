#!/usr/bin/python3
if __name__ == '__main__':
     from sys import argv
     n = len(argv)
     if n < 3:
          pass
     else:
          sum = 0
          for x in range(1, n):
               sum = sum + int(argv[x])
          print(sum)
