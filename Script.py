names = ["Sharon", "Michelle", "Juliet", "Ethan", "Kylie", "Cherish"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")
        print("Names that have been written to names.txt.")

        print("\nReading names from file:")
        with open("names.txt", "r") as file:
            for line in file:
                print(line.strip())
