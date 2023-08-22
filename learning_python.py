filename = "text_files/learning_python.txt"
with open(filename) as file_object:
    """content = file_object.read()
    print(content)"""
    
    """for line in file_object:
        print(line.rstrip())"""
        
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C')  # replacing Python with C 
    print(line.rstrip())
    
