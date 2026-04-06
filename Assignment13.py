# Pattern using while loop
# *
# **
# ***
# ****
# *****

# CLASSICAL METHOD

# n = int(input("Enter a number : "));

# i = 1;
# while i <= n:
#     print("* " * i);
#     i += 1;


# ADVANCED METHOD

n = int(input("Enter a number : "));

i = 1;
while i <= n:
    j = 1;
    while j <= i:
        print("* ", end="");
        j += 1;
    print();
    i += 1;
