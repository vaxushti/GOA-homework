start = int(input("Enter Starting Number! "))
end = int(input("Enter Ending Number! "))
for num in range(start, end + 1):
  if num % 5 == 0:
    print(num)