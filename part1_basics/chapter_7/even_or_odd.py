number = input("Enter a number, and I'll tell you if it's even of odd: ")
number = int(number)

if number % 2 == 0:  # 取模运算
    print("\nThe number "+str(number)+" is even.")
else:
    print("\nThe number "+str(number)+" is odd.")
