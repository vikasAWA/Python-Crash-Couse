filename = "text_files/alice.txt"

try:
    with open(filename, encoding='utf-8') as file_object:
        content = file_object.read()
except FileNotFoundError:
    msg = f"Sorry the file {filename} does not exist."
    print(msg)
else:
    # Count th approximate number of words in file.
    words = content.split()
    num_words = len(words)
    print(f"File {filename} has about {num_words} words.")
