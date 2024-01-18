#!/usr/bin/python3
if __name__ == "__main__":
     from calculator_1 import add, sub, mul, div
     from sys import argv
     n = len(argv)
     if n == 4:
          a, operator, b = argv[1:]
          a = int(a)
          b = int(b)
          if operator == '+':
               print("{} + {} = {}".format(a, b , add(a, b)))
          elif operator == '-':
               print("{} - {} = {}".format(a, b , sub(a, b)))
          elif operator == '*':
               print("{} * {} = {}".format(a, b , mul(a, b)))
          elif operator == '/':
               print("{} / {} = {}".format(a, b , div(a, b)))
          else:
               print("Unknown operator. Available operators: +, -, * and /")
               exit(1)
     else:
          print("Usage: ./100-my_calculator.py <a> <operator> <b>")
          exit(1)
