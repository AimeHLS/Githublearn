import json
from pathlib import Path

def is_number(input_str):
    """Check if input is a number"""
    try:
        int(input_str)
        return True
    except ValueError:
        return False

# Part1: Get user input and store it as a JSON file
favorite_number = input('Write your favorite number here: ')
while not favorite_number or not is_number(favorite_number):
    favorite_number = input(" Please enter a valid number here: ")
#convert input to json file
json_contents = json.dumps(favorite_number)

# Define the path to the file where the number will be stored and name the file
file_path = Path('favorite_number.json')

# Write json contents to the file
file_path.write_text(json_contents)

print("Your favorite number has been restored.")

# Part 2: Open the stored file and read from it.

# Define the path where the file is stored
file_path = Path ('favorite_number.json')

# Check if the file exists
if file_path.exists():
    # Read JSON content from the file
    json_contents = file_path.read_text()

    # Converet the JSON content back to a python object
    favorite_number = json.loads(json_contents)

    print(f"I know your favorite number! It's {favorite_number}")
else:
    # print("I don't know your favourite number yet."
    #       "Please run the program to store it first")
    def store_favorite_number():
        favorite_number = input("I don't know your favorite number yet. "
                                "Please write your favorite number here: ")
        json_contents = json.dumps(favorite_number)
        file_path.write_text(json_contents)
        print("Your favorite number has been stored.")
        return favorite_number


