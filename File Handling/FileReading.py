# With keyword --> Closes file automatically

# with open("file.txt", "r") as f:
#     print(f.read())

with open("file.txt", "r") as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    line5 = f.readline()
    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(line5)