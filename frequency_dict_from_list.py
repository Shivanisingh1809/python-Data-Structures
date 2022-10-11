from collections import Counter

mylist = [1, 2, 4, 45, 35, 234, 312, 3, 324, 35, 34, 523,
          412, 2, 4534, 345, 23, 1, 12, 3, 34, 13, 1, 31, 4]

print(dict(Counter(mylist))) # creates a value, frequency pairing
