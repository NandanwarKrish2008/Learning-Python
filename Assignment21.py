# Wwrite a program which takes string as input and count vowels and consonents in string

def fun(UserInput):
    vowels = "aeiouAEIOU"
    num = "0123456789"

    countvowels = 0
    countconsons = 0
    countnum = 0

    for eachChar in UserInput:
        if(eachChar in vowels):
            countvowels += 1
        elif(eachChar in num):
            countnum += 1
        else:
            countconsons += 1
    return countvowels, countconsons, countnum

Input = input("Give the input string: ")

print("Vowels, Consonants, Numbers")
print(fun(Input))