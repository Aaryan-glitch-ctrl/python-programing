import random

# Step 1: Create list of 5 odd integers using random numbers
odd_numbers = []
while len(odd_numbers) < 5:
    num = random.randint(1, 100)
    if num % 2 != 0:
        odd_numbers.append(num)

print("Step 1: List of 5 random odd integers:")
print(odd_numbers)

# Step 2: Create list of 4 even integers using random numbers
even_numbers = []
while len(even_numbers) < 4:
    num = random.randint(1, 100)
    if num % 2 == 0:
        even_numbers.append(num)

print("\nStep 2: List of 4 random even integers:")
print(even_numbers)

# Step 3: Replace the third element of odd list with even list
odd_numbers[2] = even_numbers
print("\nStep 3: After replacing the third element of odd list with even list:")
print(odd_numbers)

# Step 4: Flatten the list
flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

print("\nStep 4: Flattened list:")
print(flattened_list)

# Step 5: Sort the flattened list
flattened_list.sort()
print("\nStep 5: Sorted flattened list:")
print(flattened_list)
