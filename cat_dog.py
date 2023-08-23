filenames = ['cat.txt', 'dog.txt', 'bird.txt']

for filename in filenames:
    try:
        with open(f"text_files/{filename}") as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"File {filename} does not exist")
    else:
        print(content)