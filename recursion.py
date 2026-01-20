def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)

#

import sys
print(sys.getrecursionlimit())

#

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())