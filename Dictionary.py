# A dictionary is a built-in data type in Python used to store data in key–value pairs.

# Each key is unique and maps to a value.

# Dictionaries are mutable, meaning you can change their content after they have been created.

student = {
    "name" : "Krish",
    "age" : 18,
    "grade" : "A",
    "city" : "Surat"
}

# print(type(student)); # prints the type of the variable, which is <class 'dict'>

# print(student); # prints the entire dictionary

print(student["name"]); 
print(student["age"]);
print(student["grade"]);
print(student["city"]);

student["city"] = "Ahmedabad";
print(student["city"]);
