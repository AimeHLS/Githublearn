import json
from pathlib import Path

def greet ():
    print("Hello!")

greet()

# pass information to the function

def greet (username):

    print(f"Hello {username.title()}!")

greet('hKK')
# Without return function, there is no need for a variable. We can simply call the function directly

def learn_python(need_1, need_2):

    print("\nTo learn python well you "
          f"need understand {need_1} and its {need_2}.")

learn_python('synthax', 'logic')
learn_python('focus', 'importance')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"\n{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
# With return function, we always have to set the function to a variable.
print(musician)


names= []

def get_formatted_name(first_name, last_name):
    """Return a full name neatly formatted."""

    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name and type exit to stop:")

    f_name = input("First name: ")
    if f_name.strip().lower() == 'exit':
        break

    l_name = input("Last name: ")
    if l_name.strip().lower() == 'exit':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    names.append(formatted_name)

#1 WRITE TO THE FILE
 # Convert python object to json string
json_contents = json.dumps(names)

 # Define a path where the file is to be stored
file_path = Path("names.json")

# Write json contents to the file
file_path.write_text(json_contents)

# for name in names:
#     print(f"\nHello, {name}")
#2 OPEN JSON FILE AND READ FROM IT

# Define the path where the file is stored
file_path = Path('names.json')

# check if the file exists
if file_path.exists():

    # Read JSON content from the file
    json_contents = file_path.read_text()

    # Convert the JSON content back to a python object
    names = json.loads(json_contents)
    for name in names:
        print(f"Welcome back {name}!")
else:
    pass





unprinted_designs = ['phone case', 'robot']
completed_models = []

# while unprinted_designs:
#     currrent_design= unprinted_designs.pop()
#     print(f'\nPrinting models: {currrent_design}')

#     completed_models.append(currrent_design)

# print("\nThe following models have been printed: ")
# for completed_model in completed_models:
#     print(completed_model)

def printing_model(unprinted_designs, completed_models):
    """
    Simultate printing each design, until none are left.
    Move each design to completed_models after printing.

    """
    while unprinted_designs:
        currrent_design = unprinted_designs.pop()
        print(f'\nPrinting models: {currrent_design}')
        completed_models.append(currrent_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\nThe following models have been printed: ")

    for completed_model in completed_models:
        print(completed_model)


printing_model(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Passing an Arbitrary Number of Arguments(*args) and (**kwargs)
def arbitrary(**kwargs):
    pass





