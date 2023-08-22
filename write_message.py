filename = "text_files/programming.txt"

# Writing into a file, if does not exist wil create new file 
"""with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love Creating new games.\n")"""
    
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")