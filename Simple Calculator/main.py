from art import logo

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def div(n1, n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : div,
}

def calculator():
    print(logo)
    end = False
    num1 = int(input("Enter first number- "))

    while not end:
        num2 = int(input("Enter second number- "))
        for keys in operations:
            print(keys)

        num_operation = input("Enter operation to be performed- ")
        answer = operations[num_operation](num1, num2)
        print(f"{num1} {num_operation} {num2} = {answer}")

        choice = input(f"\nType 'y' to continue calculation with {answer} \nType 'f' to start a fresh calculation \nType 'n' to end\nEnter choice- ")
        if choice == "f":
            end = True
            calculator()
        elif choice == "n":
            print("Goodbye!!! ")
            end = True
        else :
            num1 = answer

calculator()