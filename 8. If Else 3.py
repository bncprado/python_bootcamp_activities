print("")

num = int(input("Please, type a number divisible by 3 or 7 > " ))

print("")

if num %7==0 and num %3==0:
    print ("fizzbuzz")

elif num %3==0 :
    print ("fizz") 

elif num %7==0:
    print ("buzz")

else:
    print  (num)

print("")

"""Another great example of code! You have structured your statement perfectly. 
Fizzbuzz has to go first in this situation, and you've got that down exactly! 
If fizzbuzz was written in last (as the question stated), it would likely never trigger, as "fizz" or "buzz" would be True first. Well done!

As always, you're continuing to make great use of the input function, which gives your code a lot of flexibilty, and casting it where necessary. Great work!

"""