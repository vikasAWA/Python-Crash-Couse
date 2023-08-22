filename = "text_files/one-million.txt"
with open(filename) as file_object:
    """contents = file_object.read() # Reading the whole content 
    print(contents.rstrip())"""
    
    # Reading line by line 
    """for line in file_object:
        print(line.rstrip())"""
        
    # making a list of lines from a file
    lines = file_object.readlines() # lines is a list containing line
    
"""print(lines) 
for line in lines:
    print(line.rstrip())"""
    
# Worling with files content 
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:53] + '...')
print(len(pi_string))

birthday = input("Enter Your Birthday, in fmt mmddyy: ")
if birthday in pi_string:
    print("Your Birthday apeears in first million digits of pi.")
else:
    print("Your birthday does not appear in first million digits of pi.")