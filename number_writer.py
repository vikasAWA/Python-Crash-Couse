import json

numbers = [5, 4, 5, 6, 7, 9, 1]

filename = 'json/numbers.json'

with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)