list_of_tuples = [(), (1, 2), (), (3, 4), (5, 6), ()]

# Remove empty tuples
cleaned_list = [t for t in list_of_tuples if t]

print(cleaned_list)
