#!/usr/bin/python3
if __name__ == "__main__":
     import hidden_4
     name = dir(hidden_4)
     for x in name:
          if '__' not in x:
               print(x)
