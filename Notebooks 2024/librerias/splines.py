import numpy as np
import pandas as pd
import math
from pandas.tseries.offsets import DateOffset

def B(x, k, i, t):
   if k == 0:
      return 1 if t[i] <= x < t[i+1] else 0.0
   if t[i+k] == t[i]:
      c1 = 0.0
   else:
      c1 = (x - t[i])/(t[i+k] - t[i]) * B(x, k-1, i, t)
   if t[i+k+1] == t[i+1]:
      c2 = 0.0
   else:
      c2 = (t[i+k+1] - x)/(t[i+k+1] - t[i+1]) * B(x, k-1, i+1, t)
   return c1 + c2

def bspline(x, t, c, k):
   n = len(t) - k - 1
   # n > k+1 -> n >= 1  len(t) > 2(k + 1) = 8
   assert (len(c) >= n) #and (n >= k+1)
   return sum(c[i] * B(x, k, i, t) for i in range(n))