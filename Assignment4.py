# Write a program that takes total bill amount and number of people as input and print the amount each person has to pay

total_bill = float(input("Enter total bill amount : "))

num_people = int(input("Enter number of people : "))

amount_per_person = total_bill / num_people

print("Each person has to pay : ", amount_per_person)