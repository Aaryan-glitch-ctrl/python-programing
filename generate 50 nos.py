import random

# Stage 1: Generate 50 random numbers between 1 and 30
print("Generating 50 random numbers between 1 and 30...")
numbers = [random.randint(1, 30) for _ in range(50)]

# Stage 2: Display the original list
print("\nOriginal List:")
print(numbers)

# Stage 3: Remove duplicate values
print("\nRemoving duplicate values...")
unique_numbers = list(set(numbers))

# Stage 4: Display the updated list
print("\nList after removing duplicates:")
print(unique_numbers)
