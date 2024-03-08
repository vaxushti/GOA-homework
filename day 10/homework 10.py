registred_password = "mujira777"
avtorized = "false"
while avtorized != True :
    user_input = input("please enter your pasword:")

    if user_input == registred_password:
        print("acces granted")
        avtorized + True
    else:
        print("password incorrect please try again")

        