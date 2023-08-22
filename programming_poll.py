"""Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses."""

while True:
    # ask for input
    name = input("Enter Your name (or q to quit): ")
    if name.lower() == 'q':
        break
    
    response = input("Why do you like programming? ")
    
    
    with open("text_files/programming_poll.txt", "a") as file_object:
        file_object.write(f"Responsee of {name} : {response}.\n" + "\n")