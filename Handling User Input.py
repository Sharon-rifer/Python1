while True:
    try:
        number = float(input("Enter a number"))
        print("Ypo entered:" , number)
        break
        except ValueError:
        print("Invalid input. Please enter a valid number.")