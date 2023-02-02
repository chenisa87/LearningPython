
number = eval(input("Enter a number: "))
reversedNumber = (number % 10) * 100 + (number // 100) + (number - number//100 * 100 - number % 10)

if number == reversedNumber:
    print("The number is a palindrome number.")
else:
    print("The number is not a palindrome number.")