# COUNTDOWN
import time
n = int(input("Enter a number : ")); 

print("The countdown starts now: "); 

for i in range(n, 0, -1):
    print(i); 
    time.sleep(1); 
print("Blast off!"); 
