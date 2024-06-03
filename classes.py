class Dog:
    """A simple attempt to describe dog's behavior."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        # create init method and intialiaze attributes.
        # It seems like init method belongs to the class itself

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

# The simulate the behavior that you want to see
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
# To call a class we always need a variable
print(f"My dog is {my_dog.age} years old.")

