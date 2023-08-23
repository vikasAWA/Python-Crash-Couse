def count_words(filename):
    """Count th approximate number of words in file."""
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        msg = f"The file {filename} , you are looking for does not exist."
        print(msg)
    else:
        words = content.split()
        print(f"The file {filename} has about {len(words)} words.")
        
        
if __name__ == '__main__':
    filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
    for filename in filenames:
        count_words(f"text_files/{filename}")
