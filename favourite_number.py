import json 

fav_number = input("What is your favourite number? ")

filename = 'json/favourite_number.json'
with open(filename, 'w') as file_obj:
    json.dump(fav_number, file_obj)