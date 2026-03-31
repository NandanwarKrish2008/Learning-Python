#Take diameter as input and find the area of circle

diameter = float(input("Enter the diameter of the circle : "))
radius = diameter / 2
area = 3.14 * radius * radius
print ("The area of circle is : ", area)

# Another way to calculate area
# area = 3.14 * (radius ** 2)