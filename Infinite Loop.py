# Infinite Loop in python


i = 1

while i>0:
    print(i)
    i += 1
    if i == 10001:
        break
    else:
        continue