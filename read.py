from pathlib import Path
import json

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
