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
    print("You are inside the pickling room.\n")
    print("What would you like to do?")
    print("******************\n")
    print("1. View pickling table")
    print("2. View fridge")
    print("\n******************")
    choice = input("- enter a number for your chosen option above: \n\n")
    
    if choice == "1":
        consider_pickling_table()
    elif choice == "2":
        consider_fridge()
    else:
        print("Invalid choice; please enter one of the choice numbers given above when given the prompt.")
        time.sleep(2)
        tmp = sp.call('clear', shell=True)
        consider_pickling_room()




def consider_fridge():
    """
    Give user options for fridge
    """
    print("You crack open your gently humming fridge.")
    print("What would you like to do?")
    print("(enter an option)")
    print("1. Survey items on fridge shelves")
    print("2. Eat a pickle")
    print("n. Close fridge")


def consider_pickling_table():
    """
    Give user options for pickling table
    """
    print("You approach the pickling table.")
    print("What would you like to do?")
    print("(enter an option)")

    print("1. Survey pickling table items")
    print("2. Pick out an empty jar")
    print("3. Put out a bowl")
    print("4. Put out ingredients")

    print("5. Wash item in sink")
    print("6. Boil an item for 15m in hot water")
    print("")
    print("")
    print("n. Move across the pickling room")







"""
cucumber1 = Cucumber()
print(cucumber1.describe())
"""

move_to(location)
