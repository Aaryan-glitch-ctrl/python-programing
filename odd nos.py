import random

# Stage 1: Generate 20 random integers
print("Generating 20 random integers between 1 and 50...")
numbers = [random.randint(1, 50) for _ in range(20)]

# Stage 2: Display the generated list
print("List generated successfully!")
print("The list of random numbers is:")
print(numbers)

# Stage 3: Ask user to enter a number to search
search_number = int(input("\nEnter a number to find its position(s) in the list: "))

# Stage 4: Find all positions of the entered number
positions = [index for index, value in enumerate(numbers) if value == search_number]

# Stage 5: Display results
if positions:
    print(f"\nThe number {search_number} is found at position(s): {positions}")
else:
    print(f"\nThe number {search_number} is not found in the list.")
