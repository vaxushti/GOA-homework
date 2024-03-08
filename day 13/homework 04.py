user_input = input("Enter Right Password! ")

password = "abc123"


while True != password:
  if user_input != password:
    print("Access Denied!")
    break

  elif user_input == password:
    print("Acces Granted!")
    break
  
  else:
    print("Gotta Try Again!")