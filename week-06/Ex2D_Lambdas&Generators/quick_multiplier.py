# Cesar Alcantar
# Exercise 2.D - Lambdas and Generators
# quick_multiplier.py


# Step 1: Create a lambda function that doubles a value
doubler = lambda n: n * 2

# Test the doubler with different values
print("Doubler:")
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))


# Step 2: Create a lambda function that triples a value
tripler = lambda n: n * 3

# Test the tripler with different values
print("\nTripler:")
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


# Step 3: Create a multiplier function
def multiplier(n):
    return lambda x: x * n


# Step 4: Create multiplier variables from 4 through 10
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)


# Step 5: Test each multiplier
print("\nQuadrupler:")
print(quadrupler(5))

print("\nQuintupler:")
print(quintupler(5))

print("\nSextupler:")
print(sextupler(5))

print("\nSeptupler:")
print(septupler(5))

print("\nOctupler:")
print(octupler(5))

print("\nNonupler:")
print(nonupler(5))

print("\nDecupler:")
print(decupler(5))
