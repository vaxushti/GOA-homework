num = int(input("Enter Number! "))

if num % 3 == 0:
  print("Fizz")
elif num % 5 == 0:
  print("Buzz")
elif num % 5 and 3 == 0:
  print("FizzBuzz")
else:
  print(num)