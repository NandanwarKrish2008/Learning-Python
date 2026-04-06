# Print numbers from 1 to 50 but print "RANDOM" for multiples of 5

for i in range(1, 51, 1):
    if i % 5 == 0:
        print("RANDOM");
    else:
        print(i);