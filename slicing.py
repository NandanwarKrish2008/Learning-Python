# Slicing let you access a particular part of a string
# Syntax : string_name[start_index:end_index] where end_index is excluded

name = "GulabJamun"
print(name[0:3])  
print(name[3:5])  

print(name[:5])
print(name[5:])
print(name[:])

# Negative indexing
# K   R  I  S  H  N  A
# -7  -6 -5 -4 -3 -2 -1
# The method of slicing string is also same as above we just need to replace the positive index with negative index