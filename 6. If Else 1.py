print("")

password = input("Please, type your password > ")

passlenght = len(password)

print("")

if passlenght < 8:
    print (f"Your password is too short. Please, run the code again and retype a new password with at least 8 characters")

    print("")

else: 

    print (f"""Your new password is "{password}" """)

    print("")