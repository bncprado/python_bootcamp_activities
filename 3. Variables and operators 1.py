#addition .It adds the typed numbers in the code

print (" ----------------------")
print ("| ARITHMETIC OPERATORS |")
print (" ----------------------")
print("                                                      ")
print ("This is the ADDITION example:")
print("                                                      ")
print ("Type the numbers to ADD them:")
print("                                                      ")
addnum1 = int(input("Please type number 1    > "))
addnum2 = int(input("Please type number 2    > "))

addresult = addnum1 + addnum2
print("                                                      ")
print("The result is:".upper(), addnum1,"+",addnum2,"=", addresult)
print("                                                      ")
print ("---------------------------------------------------------------------------")

#subtraction. It subtracts the typed numbers in the code

print("                                                      ")
print ("This is the SUBTRACTION example:")
print("                                                      ")
print ("Type the numbers to SUBTRACT them:")
print("                                                      ")
subtnum1 = int(input("Please type number 1    > "))
subtnum2 = int(input("Please type number 2    > "))

subtresult = subtnum1 - subtnum2
print("                                                      ")
print ("The result is:".upper(),subtnum1,"-",subtnum2,"=",subtresult)
print("                                                      ")
print ("---------------------------------------------------------------------------")
#Multiplication. It multiplies the typed numbers in the code

print("                                                      ")
print ("This is the MULTIPLICATION example:")
print("                                                      ")
print ("Type the numbers to MULTIPLY them:")
print("                                                      ")
multnum1 = int(input("Please type number 1    > "))
multnum2 = int(input("Please type number 2    > "))

multresult = multnum1 * multnum2
print("                                                      ")
print ("The result is:".upper(),multnum1,"*",multnum2,"=",multresult)
print("                                                      ")
print ("---------------------------------------------------------------------------")

#Exponential. It multiplies the typed numbers exponentialy in the code

print("                                                      ")
print ("This is the EXPONENTIAL example:")
print("                                                      ")
print ("Type the numbers to multiply them EXPONENTIALY:")
print("                                                      ")
expnum1 = int(input("Please type number 1    > "))
expnum2 = int(input("Please type number 2    > "))

expresult = expnum1 ** expnum2
print("                                                      ")
print ("The result is:".upper(),expnum1,"**",expnum2,"=",expresult)
print("                                                      ")
print ("---------------------------------------------------------------------------")

#Division. It divides the typed numbers in the code

print("                                                      ")
print ("This is the DIVISION example:")
print("                                                      ")
print ("Type the numbers to DIVIDE them:")
print("                                                      ")
divnum1 = int(input("Please type number 1    > "))
divnum2 = int(input("Please type number 2    > "))

divresult = divnum1 / divnum2
print("                                                      ")
print ("The result is:".upper(),divnum1,"**",divnum2,"=",divresult)
print("                                                      ")
print ("---------------------------------------------------------------------------")

#Modulo (remainder). It divides the numbers using only integers and shows ONLY what lasts of that division.
#for an instance 10/3 = 3 and 1 is the remainder. So it will show number 1

print("                                                      ")
print ("This is the REMAINDER example:")
print("                                                      ")
print ("Type the numbers to show the REMAINDER of the division:")
print("                                                      ")
modnum1 = int(input("Please type number 1    > "))
modnum2 = int(input("Please type number 2    > "))

modresult = modnum1 % modnum2
print("                                                      ")
print ("The result is:".upper(),modnum1,"%",modnum2,"=",modresult)
print("                                                      ")
print ("---------------------------------------------------------------------------")