def print_reverse_natural(n):
    for i in range(n, 0, -1):
        print(i, end=" ")
    print() 
n = 10
print(f"The first {n} natural numbers in reverse are:")
print_reverse_natural(n)
