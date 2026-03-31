# Take input in celsius and convert it to fahrenheit and kelvin (Use explicit type casting and arithmetic operators)


celsius = input("Enter temperature in celsius : ")
celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Temperature in fahrenheit : ", fahrenheit)
print("Temperature in kelvin : ", kelvin)

