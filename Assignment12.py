# Calculate factorial of n numbers

n = int(input("Enter a number: "));
fact = 1;

while n >= 1:
    fact *= n;
    n -= 1;

print(f"The fatorial is : {fact}"); 
