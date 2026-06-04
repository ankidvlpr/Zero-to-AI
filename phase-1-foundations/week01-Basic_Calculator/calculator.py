print("Program Started! Type 'exit' to quit.\n")

while True:

    user_input = input("Enter calculation (example: 2 + 3): ")

    if user_input.lower() == "exit":
        print("Good Bye!")
        break

    parts = user_input.split()

    if len(parts) != 3:
        print(" Please! Write in format (example: 2 + 3)")
        continue

    num1, operator, num2 = parts

    try:

        num1 = float(num1)
        num2 = float(num2)

        if operator == "+":
            print(num1 + num2)

        elif operator == "*":
            print(num1 * num2)

        elif operator == "-":
            print(num1 - num2)

        elif operator == "/":

            if num2 == 0:
                print("Error: number cant be divide by zero")
                continue

            print(num1 / num2)

        else:
            print("invalid operator")

    except ValueError:

        print("Error: please type valid numbers")