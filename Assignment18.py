# Multiplication Table using for loop

n = int(input("Enter a number : "));

for i in range(1, 11, 1):
    print(f"{n} x {i} = {n * i}");