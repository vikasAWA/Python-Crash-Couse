from name_function import get_formatted_name

print("Enter q any time to quit\n")

while True:
    first = input("\nEnter first name: ")
    if first == "q":
        break 
    last = input("Enter last name: ")
    if last == 'q':
        break
    name = get_formatted_name(first, last)
    print(f"\t Neatly formatted Name: {name}")
        