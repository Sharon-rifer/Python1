def classify_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

    while True:
        try:
            user_input = int(input("Enter an integer: "))
            break
            except ValueError:
            print("Invalid input. Please enter a valid integer.")
