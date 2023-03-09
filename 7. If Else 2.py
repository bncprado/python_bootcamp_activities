## my solution

# print("")

# num = int(input("Type here your num > "))

# numCheck = num % 3==0 or num %5 == 0

# print("")

# if numCheck == True:
    
#     print ("This number is divisible by 3 or 5")

#     print("")

# else:
    
#     print ("This number is not divisible by 3 or 5")

#     print("")

#-------------------------------------------------------------------

print("")

num = int(input("Type here your num > "))

print("")

if num % 3==0 or num %5 == 0:
    
    print ("This number is divisible by 3 or 5")

    print("")

else:
    
    print ("This number is not divisible by 3 or 5")

    print("")

"""You've made fantastic use of the logical operator or to write a great piece of code, 
I tested it with many numbers and it always gave me the correct result. 
You're continuing to use input well, casting it when necessary to an integer so we can use mathmatical operators.

You're also showing great use of the Boolean data type - by the way you've written your code, it shows you understand 
fully the concept of comparisons evaluating down to a True or False value. Well done!

You don't necessarily need to save that Boolean to a variable, as you have. 
If you're not using that True value elsewhere, you could simplify your code from:

numCheck = num % 3==0 or num %5 == 0

print("")

if numCheck == True:

to

if num % 3==0 or num %5 == 0:

Great work!"""