user_number1 = int(input("Enter the first number: "))
user_number2 = int(input("Enter the second number: "))

def numbers():
    select = input("select(+,-,/,*): ")
    if select == "+":
        answer = user_number1 + user_number2
        print(answer)
    elif select == "-":
        answer = user_number1 - user_number2
        print(answer)
    elif select == "/":
        answer = user_number1 / user_number2
        print(answer)
    elif select == "*":
        answer = user_number1 * user_number2
        print(answer)
    else:
        TypeError("Wrong selection")

numbers()

