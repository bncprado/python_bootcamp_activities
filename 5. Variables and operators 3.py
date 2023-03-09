applePricePence= 25

applePricePound= 0.25

print("")

numberOfApples = int(input("Please, type how many apples you'd like to buy > "))

totalAmountPence = applePricePence*numberOfApples

totalAmountPound = applePricePound*numberOfApples

print("")

if  numberOfApples <4:
    print (f"The total price for {numberOfApples} apples is {totalAmountPence}p")
else:
    print (f"The total price for {numberOfApples} apples is £{totalAmountPound}")
    
print("")