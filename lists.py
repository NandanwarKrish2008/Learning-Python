# Lists in python
# LISTS ARE MUTABLE (CAN BE CHANGED) AND ORDERED (MAINTAIN THE ORDER OF ELEMENTS)

food = ["Pizza", "Burger", "Pasta", "Salad", "Sushi"];

# print(food); # prints the entire list
# print(food[0]); # prints the first item in the list
# print(food[1]); # prints the second item in the list
# print(food[-1]); # prints the last item in the list

# print(len(food)); # prints the length of the list
# print(food[0:3]); # prints the first three items in the list


# food[3] = "Fries"; # changes the fourth item in the list to "Fries"
# print(food[3]); 


# METHODS IN LISTS

food.append("Ice Cream"); # adds "Ice Cream" to the end of the list
print(food);

food.sort(); # sorts the list in ascending order
print(food);

food.insert(0, "Sandwich"); # inserts "Sandwich" at index 0