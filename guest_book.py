while True: 
    name = input("What's your name? ")
    print(f"Wlcome {name}!")
    
    with open("text_files/guest_book.txt", "a") as file_object:
        file_object.write(f"{name} has logged in." + '\n')