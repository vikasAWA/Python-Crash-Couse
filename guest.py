filename = "text_files/guest.txt"

with open(filename, 'a') as file_object:
    file_object.write(input('Name:') + '\n')
    
