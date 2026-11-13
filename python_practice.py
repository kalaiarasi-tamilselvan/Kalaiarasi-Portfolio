# Python Practice Programs
# Author: Kalaiarasi T


# 1. Even or Odd
def even_or_odd():
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")


# 2. Factorial
def factorial():
    n = int(input("Enter a number: "))
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("Factorial of", n, "is", result)


# 3. Simple Calculator
def calculator():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operation")


# 4. Palindrome Check
def palindrome():
    text = input("Enter a word: ").lower()
    if text == text[::-1]:
        print(text, "is a palindrome")
    else:
        print(text, "is not a palindrome")


# 5. Fibonacci Series
def fibonacci():
    n = int(input("How many terms? "))
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# Menu
def main():
    while True:
        print("\n--- Python Practice Programs ---")
        print("1. Even or Odd")
        print("2. Factorial")
        print("3. Calculator")
        print("4. Palindrome Check")
        print("5. Fibonacci Series")
        print("6. Exit")
        choice = input("Choose (1-6): ")

        if choice == "1":
            even_or_odd()
        elif choice == "2":
            factorial()
        elif choice == "3":
            calculator()
        elif choice == "4":
            palindrome()
        elif choice == "5":
            fibonacci()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again")


main()
