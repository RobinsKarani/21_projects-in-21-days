import random

# Using random.randrange(-5, 11)
r = random.randrange(-5, 11)  
# random.randrange() generates a random integer in the range from -5 to 10 (11 is exclusive)
# So the possible values for r are: -5, -4, -3, ..., 9, 10
print(r)

# Using random.randint(-5, 11)
r2 = random.randint(-5, 11)
# random.randint() generates a random integer in the range from -5 to 11 (both inclusive)
# So the possible values for r2 are: -5, -4, -3, ..., 9, 10, 11
print(r2)
