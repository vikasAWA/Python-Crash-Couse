print("Give me teo numbers, I will add them for You.")

while True:
    try:
        first_number = float(input("\nFirst Number: "))
        second_number = float(input("Second Number: "))

    except ValueError:
        print("You entered text not a number.")
    else:
        print(first_number+second_number)
        break