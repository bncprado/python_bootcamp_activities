print("")

print ("What is the capital of England?")

print("")

answer = input("Type your answer here > ")

print("")

if answer == "London" or answer == "london":
    print (f"Correct! The answer is {answer.title()}")
else:
    print (f"Incorrect! The correct answer is London, not {answer.title()}")

print("")

"""For this activity, you were asked to fix the incorrect code, which you have done. 
This shows your skills in testing, reading the error messages given in terminal, and debugging as necessary.

You've made great use of the logical operator "or" to allow multiple correct answers - London and london. 
This was a great choice! You could have also used a string method like .capitalize() to force the user's input to match your expected answer. 
You showcased this in your f string, which was great.

You're writting very efficient code, taking users into account at all times, and giving very clear responses. Well done!"""