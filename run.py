import time
import subprocess as sp

location = "pickling room"


# storage & display areas
fridge = [[], [], []]
pickling_table = []

# food items and combined ingredient arrays
spices = []
garlic = "garlic"
dill = "dill"
mustard_seeds = "mustard seeds"

picklingbrine = []
salt = "salt"
sugar = "sugar"
water = "water"
vinegar = "vinegar"


class Jar:
    """jar class"""
    def __init__(self):
        # properties
        self.size = "medium"
        self.label = ""
        self.contents = []
        self.lid = "on"

    def describe(self):
        description = f"description: \nsize: {self.size}\nlabel: {self.label}\ncontents: {self.contents}\nlid: {self.lid}"
        return description

    def open():
        self.lid = "off"

    def close():
        self.lid = "on"

    # def insert(items):

    # def fill(items):


class Cucumber:
    def __init__(self):
        self.pickledeness = "fresh"
        self.crunch = "very crunchy"

    def describe(self):
        description = f"description: \npickledness: {self.pickledeness}\ncrunch: {self.crunch}"
        return description


def move_to(destination):
    """
    move around the room
    """
    if destination == "pickling room":
        # run pickling room option script
        location = "pickling room"
        consider_pickling_room()
    elif destination == "fridge":
        # run fridge option script
        location = "fridge"
        consider_fridge()
    elif destination == "pickling table":
        # run pickling table option script
        location = "pickling table"
        consider_pickling_table()
    else:
        print("Where are you?")
        print("You have floated away")
        print("> Move back to pickling room")


def consider_pickling_room():
    """
    Give user options for pickling room
    """
    options = [1, 2]
    print("You are inside the pickling room.\n")
    print("What would you like to do?")
    print("******************\n")
    print("1. View pickling table")
    print("2. View fridge")
    choice = get_input(options)
    
    if choice == "1":
        consider_pickling_table()
    elif choice == "2":
        consider_fridge()
    else:
        """
        print("Invalid choice; please enter one of the choice numbers given above when given the prompt.")
        time.sleep(3)
        tmp = sp.call('clear', shell=True)
        """
        consider_pickling_room()





def consider_fridge():
    """
    Give user options for fridge
    """
    options = [1,2,3]
    print("You crack open your gently humming fridge.")
    print("What would you like to do?")
    print("********************")
    print("1. Survey items on fridge shelves")
    print("2. Eat a pickle")
    print("3. Close fridge")
    choice = get_input(options)

    if choice == "3":
        consider_pickling_room()


def consider_pickling_table():
    """
    Give user options for pickling table
    """
    options = [1,2,3,4,5,6,7]
    print("You approach the pickling table.")
    print("What would you like to do?")
    print("****************")

    print("1. Survey pickling table items")
    print("2. Pick out an empty jar")
    print("3. Put out a bowl")
    print("4. Put out ingredients")

    print("5. Wash item in sink")
    print("6. Boil an item for 15m in hot water")
    print("7. Move across the pickling room")
    choice = get_input(options)

    if choice == "7":
        consider_pickling_room()


def get_input(options):
    print("\n- enter a number for one of the options: \n")
    choice = input("******************\n\n")

    #print(type(int(choice)))
    validated = validate_input(choice, options)
    if validated is True:
        print("\n - A valid choice!\n")
    else:
        print("Input was invalid")
    return choice


def validate_input(choiceval, optionlist):
    """
    function for validating user input for multiple choice segments
    """

    try:
        intval = int(choiceval)
        if isinstance(intval, int) is False:
            raise ValueError(
                f"The value you entered was not a whole number. You entered {choiceval}."
            )
        choiceisoption = False
        for option in optionlist:
            if intval == option:
                choiceisoption = True
                break
        if choiceisoption == False:
            raise ValueError(
                f"The value you entered was not one of the options given. You entered {choiceval}."
            )
    except ValueError as e:
        print(f"Invalid input: {e}, Please enter one of the numbered choices.")
        return False
    except ValueError as e:
        print(f"Invalid input: {e}, Please enter one of the numbered choices.")
        return False    
    else:
        return True


def test(input):
    """
    testing type conversion
    fails unless is valid int
    if string or float or non int value ...
    if this fails
        print Error("yo it's not an int. It looks like string/float/boolean")
    else:
        print("congrats it's an int")
    """
    print("Input type conversion attempt- type is:" + type(int(input)))
    print("should be int")
    




"""
cucumber1 = Cucumber()
print(cucumber1.describe())
"""

move_to(location)

