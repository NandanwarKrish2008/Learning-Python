# Take 3 numbers as input and store them in a list. Then sort the list in ascending order and print the sorted list.and find maximum and minimum number in the list.and also find the length of the list.


num1 = float(input("Enter the first number: "));
num2 = float(input("Enter the second number: "));
num3 = float(input("Enter the third number: "));

numbers = [num1, num2, num3];
numbers.sort(); # sorts the list in ascending order
print("Sorted list: ", numbers);
print("Maximum number: ", max(numbers)); # finds the maximum number in the list
print("Minimum number: ", min(numbers)); # finds the minimum number in the list
print("Length of the list: ", len(numbers)); # finds the length of the list

