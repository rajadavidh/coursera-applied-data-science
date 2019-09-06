"""
Given a 6x6 NumPy array r, which of the following options would slice the shaded elements?

Shaded elements is `[0, 7, 14, 21, 28, 35]`
"""
import numpy as np
r = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29], [30, 31, 32, 33, 34, 35]])

# Solution
r.reshape(36)[::7]
