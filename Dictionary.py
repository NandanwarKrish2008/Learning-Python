# A dictionary is a built-in data type in Python used to store data in key–value pairs.

# Each key is unique and maps to a value.

# Dictionaries are mutable, meaning you can change their content after they have been created.

student = {
    "name" : "Krish",
    "age" : 18,
    "roll number" : 101,
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


student["FavSubject"] = "Maths";
student["Country"] = "India";

print(student);

# Removing Items from a Dictionary

# METHOD-01 : del keyword
# del student["roll number"]; # deletes the key "roll number" and its associated value from the dictionary
# print(student);


# METHOD-02 : pop() method
student.pop("roll number"); 
print(student);