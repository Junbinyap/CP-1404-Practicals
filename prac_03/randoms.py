import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
Line 1: The smallest number is 5 and the largest is 20.
Line 2: The smallest number is 3 and the line 2 cannot produce 4.
Line 3: The smallest number is 2.5 and the largest 5.5.
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))