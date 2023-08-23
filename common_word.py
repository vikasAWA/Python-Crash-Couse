filenames = ['little_women.txt', 'alice.txt', 'sidhartha.txt']

for filename in filenames:
    try:
        with open(f"text_files/{filename}", encoding='utf-8') as file_object:
            content = file_object.read()
            print(f"The word 'the' appears in {filename}, {content.count('the')} times")
    except FileNotFoundError:
        print(f"File {filename} does not exist.")