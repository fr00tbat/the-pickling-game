"""
The Pickling Game
"""



#########################################################
#########################################################
#########################################################
# Main function

def main():
    """
    Main method
    """
    location = "pickling room"

    move_to(location)


#########################################################
#########################################################
#########################################################
# some classes

class Jar:
    """Jar class"""


    def __init__(self, batch):
        # properties
        self.size = "medium"
        self.batch = batch
        self.label = ""
        self.contents = []
        self.lid = "on"
        self.disinfected = False
        self.agitated = False
        self.age = 0
        self.timestamp = 0

    def __str__(self):
        return f"jar with label {self.label}"

    def __repr__(self):
        return f"jar"

    def describe(self):
        """get description of jar"""
        description = {
            "batch": self.batch,
            "age": self.age,
            "label": self.label
            # "made-on:" self.timestamp
        }
        return description

    


    def open(self):
        """remove jar lid"""
        self.lid = "off"

    def close(self):
        """screw on jar lid"""
        self.lid = "on"

    def insert(self, chosen_item):
        """
        function to insert items into the jar
        Might adjust to insert sets of premixed items:
        - a list of 5 cucumbers
        - a list of spices
        - a list of brine ingredients
        """

        self.contents.append(chosen_item)
        for item in pickling_table:
            if item == chosen_item:
                pickling_table.remove(item)


class Cucumber:
    """Cucumber class"""
    def __init__(self):
        # Cucumber properties
        self.pickledeness = "fresh"
        self.crunch = "very crunchy"
        self.washed = "unwashed"
        self.tastiness = "moderate"
        self.contaminated = False


    def __str__(self):
        return f"cucumber"


    def __repr__(self):
        return f"cucumber"


    def describe(self):
        """get description cucumber"""
        description = f"description: \npickledness: {self.pickledeness}\ncrunch: {self.crunch}\nwashed: {self.washed}"
        return description


#########################################################
#########################################################
#########################################################
# Jar management

def spawn_jars(empty_jars):
    """
    function for spawning a new set of empty jar objects
    """
    # jar_count = 12
    jar1 = Jar(1)
    jar2 = Jar(2)
    jar3 = Jar(3)
    jar4 = Jar(4)
    jar5 = Jar(5)
    jar6 = Jar(6)
    jar7 = Jar(7)
    jar8 = Jar(8)
    jar9 = Jar(9)
    jar10 = Jar(10)
    jar11 = Jar(11)
    jar12 = Jar(12)

    jars = (jar1, jar2, jar3, jar4, jar5, jar6, jar7, jar8, jar9, jar10, jar11, jar12)
    for jar in jars:
        empty_jars.append(jar)
    print("jars spawned")
    return empty_jars


def print_empty_jars(empty_jars):
    """function to print details of empty jars left"""
    for i in range(len(empty_jars)):
        print(i)
        jaritem = empty_jars[i].describe()
        print(jaritem)


def count_empty_jars(empty_jars):
    """
    function for counting empty jars
    """
    jar_count = 0
    for i in range(len(empty_jars)):
        if isinstance(empty_jars[i], Jar):
            jar_count = jar_count + 1
    return jar_count


def get_jar(pickling_table, empty_jars):
    """ function to retrieve new jar and put it on the pickling table"""

    jar_on_table = False
    for item in pickling_table:
        if isinstance(item, Jar):
            jar_on_table = True
    if jar_on_table:
        print("You already have a jar on the table.\n")
        return None

    emptjars = []
    emptjars = empty_jars
    new_jar = None
    for i in range(len(emptjars)):
        # print(isinstance(emptjars[i], Jar))
        if isinstance(emptjars[i], Jar):
            new_jar = emptjars[i]
            # print(new_jar)
            emptjars[i] = 0
            empty_jars = emptjars
            break
    if new_jar is not None:
        pickling_table.append(new_jar)
        current_jar = pickling_table[-1]
        writelabel = input("Please write a descriptive label for your chosen jar:\n")
        new_jar.label = writelabel
        print(new_jar.describe())
        print(f"Pickling table contents at present:\n {pickling_table}\n")
        return(pickling_table, emptjars)
    else:
        print("new jar did not get assigned")
        return(new_jar)


def test(usrinput):
    """
    testing type conversion
    fails unless is valid int
    if string or float or non int value ...
    if this fails
        print Error("yo it's not an int. It looks like string/float/boolean")
    else:
        print("congrats it's an int")
    """
    print("Input type conversion attempt- type is:" + type(int(usrinput)))
    print("should be int")


#########################################################
#########################################################
#########################################################
# Navigational and observational functions

def move_to(location):
    """
    move around the room
    """
    destination = location
    # storage_areas = game_state[0]
    if destination == "pickling room":
        # run pickling room option script
        location = destination
        consider_pickling_room()
    elif destination == "fridge":
        # run fridge option script
        location = destination
        consider_fridge(storage_areas)
    elif destination == "pickling table":
        # run pickling table option script
        location = destination
        consider_pickling_table(storage_areas)
    else:
        print("Where are you?")
        print("You have floated away")
        print("> Move back to pickling room")
        consider_pickling_room()


def consider_pickling_room():
    """
    Give user options for pickling room
    """
    options = [1, 2]
    print("You are inside the pickling room.\n")
    print("What would you like to do?")
    print("**********************************")
    print("1. View pickling table")
    print("2. View fridge")
    choice = get_input(options)
    if choice is False:
        consider_pickling_room()

    if choice == "1":
        consider_pickling_table()
    elif choice == "2":
        consider_fridge()
    else:
        consider_pickling_room()


def consider_fridge():
    """
    Give user options for fridge
    """
    global current_jar
    global current_pickle
    options = [1,2,3]
    print("You have cracked open your gently humming fridge.")
    print("What would you like to do?")
    print("************************************")
    print("1. Survey items on fridge shelves")
    print("2. Eat a pickle")
    print("3. Close fridge")
    choice = get_input(options)
    if choice is False:
        consider_fridge()

    if choice == "1":
        look_in_fridge()
    elif choice == "2":
        current_jar = pick_a_jar()
        current_pickle = get_pickle(current_jar)
        eat_pickle(current_pickle)
    if choice == "3":
        consider_pickling_room()
    else:
        consider_fridge()
    consider_fridge()


def consider_pickling_table():
    """
    Give user options for pickling table
    """
    jar_on_table = False
    global current_jar
    for item in pickling_table:
        if isinstance(item, Jar):
            jar_on_table = True
            current_jar = item

    if jar_on_table is False:
        options = [1,2,3,4,5,6,7]
    else:
        options = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    print("You approach the pickling table.")
    print("What would you like to do?")
    print("********************************")

    print("1. Move across the pickling room")
    print("2. Survey pickling table items")
    print("3. Pick out an empty jar")
    print("4. Put out ingredients")
    print("5. Wash item in sink")
    print("6. Boil an item for 15m in hot water")

    if jar_on_table:
        print("7. Open jar lid")
        print("8. Close jar lid")
        print("9. Put items in jar")
        print("10. Study items in jar")
        print("11. Shake jar")
        print("12. Store jar")
        print("13. Jar stats")
        print("14. Cookbook")

    choice = get_input(options)
    # rerun current function on invalid input
    if choice is False:
        consider_pickling_table()

    # normal menu
    if choice == "1":
        consider_pickling_room()
    elif choice == "2":
        survey_table(pickling_table)
    elif choice == "3":
        get_jar(pickling_table, empty_jars)
    elif choice == "4":
        study_press()
    elif choice == "5":
        what_to_wash()
    elif choice == "6":
        what_to_boil()
    # expanded menu
    elif choice =="7":
        for item in pickling_table:
            if isinstance(item, Jar):
                item.open()
    elif choice =="8":
        for item in pickling_table:
            if isinstance(item, Jar):
                item.close()
    elif choice == "9":
        for item in pickling_table:
            if isinstance(item, Jar):
                choose_to_insert()
    elif choice == "10":
        study_jar_contents()
    elif choice == "11":
        shake_jar()
    elif choice == "12":
        fridge.append(current_jar)
        for item in pickling_table:
            if isinstance(item, Jar):
                pickling_table.remove(item)
    elif choice == "13":
        jar_stats()
    elif choice =="14":
        read_cookbook()
    consider_pickling_table()


#########################################################
#########################################################
#########################################################
# Fridge operations

def look_in_fridge():
    """
    Function to look in fridge
    """
    # print label of each jar
    # details - batch, label, age?
    print("Your fridge proudly displays its jar collection:")
    jar_options = []

    for i in range(len(fridge)):
        if isinstance(fridge[i], Jar):
            print(f"\n{i}. {fridge[i].describe()}")
            jar_options.append(int(i))            
    print("\n")
    return jar_options


def pick_a_jar():
    """
    Function to pick jar to taste a pickle from
    """
    global current_jar
    # prompt user
    # display jars
    # choose a jar
    # eat pickle
    # print results
    jar_options = []
    print("Pick a jar from the fridge:")
    jar_options = look_in_fridge()
    print("Which jar would you like to taste a pickle from? \n")
    choice = int(get_input(jar_options))
    current_jar = fridge[choice]
    return current_jar


def get_pickle(jar):
    """
    Function to get a pickle from a jar
    """
    global current_pickle
    pickle_index = 0
    pickle_present = True
    for i in range(len(jar.contents)):
        if isinstance(jar.contents[i], Cucumber):
            current_pickle = jar.contents[i]
            pickle_index = i
            break
        # if none of the contents are of Class Cucumber:
        if i == len(jar.contents):
            pickle_present = False
            print("There are no pickles left in this jar!")
    
    print("You get a pickle from the jar.")
    # pickles in jar should be removed as eaten
    jar.contents.remove(jar.contents[pickle_index])
    return current_pickle


def eat_pickle(pickle):
    """Eat a pickle from the jar"""
    # Fix needed: needs to return current_pickle not None
    global current_pickle
    print("You eat the pickle:\n")
    print(pickle.describe())
    print("\n")



def populate_test_jars_fridge():
    global empty_jars
    global current_jar
    global fridge
    for i in range(5):
        current_jar = empty_jars[i]
        empty_jars[i] = 0
        current_jar.batch = i
        current_jar.label = "Here's one I made earlier"
        current_jar.contents = [salt, sugar, water, vinegar, garlic, dill, mustard_seeds]
        current_jar.disinfected = True
        current_jar.agitated = True
        current_jar.age = 5
        for k in range(5):
            cucumber = Cucumber()
            current_jar.contents.append(cucumber)
        for j in range(5):
            current_jar.contents[7+j].pickledeness = "pickled"
            current_jar.contents[7+j].crunch = "very crunchy"
            current_jar.contents[7+j].washed = "washed"
        fridge.append(current_jar)



#########################################################
#########################################################
#########################################################
# Press operations

def study_press():
    print("The following items are in the press:")
    for item in press:
        print(item)
    print("Some fresh cucumbers \n")
    print("Which would you like to take out?")
    for i in range(len(press)):
        print(f"" + str(i) + ". " + press[i])
    print(f"" + str(len(press)) + ". Some fresh cucumbers")
    print("9. Take some of everything and put it on the table")

    options = [0,1,2,3,4,5,6,7,8,9]
    choice = get_input(options)
    if choice is False:
        study_press()

    if choice == "0":
        pickling_table.append(press[int(choice)])
    elif choice == "1":
        pickling_table.append(press[int(choice)])
    elif choice == "2":
        pickling_table.append(press[int(choice)])
    elif choice == "3":
        pickling_table.append(press[int(choice)])
    elif choice == "4":
        pickling_table.append(press[int(choice)])
    elif choice == "5":
        pickling_table.append(press[int(choice)])
    elif choice == "6":
        pickling_table.append(press[int(choice)])
    elif choice == "7":
        pickling_table.append(press[int(choice)])
    elif choice == "8":
        cucumber = Cucumber()
        for i in range(5):
            pickling_table.append(cucumber)
    elif choice == "9":
        for i in range(len(press)):
            pickling_table.append(press[i])
        cucumber = Cucumber()
        for i in range(5):
            pickling_table.append(cucumber)





#########################################################
#########################################################
#########################################################
# Pickling table operations

def survey_table(pickling_table):
    """
    function to list contents of pickling table
    """
    print("You survey the pickling table.")
    if pickling_table == []:
        print("The pickling table is devoid of items at present.\n")
    else:
        print("The items on the table are as follows:")
        print(pickling_table)
        return pickling_table
        # print("\n")



def what_to_wash():
    """
    function to choose what to wash
    """
    options = []
    if pickling_table != []:
        print("What item would you like to wash?\n")
        survey_table(pickling_table)

        for i in range(len(pickling_table)):
            if isinstance(pickling_table[i], (Cucumber, Jar)):
                print(f"" + str(i) + ". " + pickling_table[i].__repr__())
            else:
                print(f"" + str(i) + ". " + pickling_table[i])
        for i in range(len(pickling_table)):
            options.append(i)

        choice = get_input(options)
        choice = int(choice)
        print(f"1.choice is : " + str(choice))
        print(type(choice))
        if choice is False:
            what_to_wash()
        # if choice is an index in the pickling_table list:    
        elif (choice >= 0 and choice <= len(pickling_table)):
            print(f"2.choice is : " + str(choice))
            if isinstance(pickling_table[int(choice)], Cucumber):
                wash(pickling_table[int(choice)])
            elif isinstance(pickling_table[int(choice)], Jar):
                print(f"You have washed the " + pickling_table[int(choice)].__repr__() + " thoroughly!\n")
            else:
                print(f"You have washed the " + pickling_table[int(choice)] + " thoroughly!\n")
    else:
        print("There is nothing on the pickling table to wash")


def wash(item):
    """
    function to wash items
    """
    item.washed = True
    print(item.describe())


def what_to_boil():
    """
    function to choose what to boil
    """
    options = []
    if pickling_table != []:
        print("What item would you like to boil?\n")
        survey_table(pickling_table)

        for i in range(len(pickling_table)):
            if isinstance(pickling_table[i], (Jar, Cucumber)):
                print(f"" + str(i) + ". " + pickling_table[i].__repr__())
            else:
                print(f"" + str(i) + ". " + pickling_table[i])
        for i in range(len(pickling_table)):
            options.append(i)

        choice = get_input(options)
        choice = int(choice)
        if choice is False:
            what_to_boil()
        # if choice is an index in the pickling_table list    
        elif (choice >= 0 and choice <= len(pickling_table)):
            if isinstance(pickling_table[int(choice)], Jar):
                boil(pickling_table[int(choice)])
            else:
                print(f"You have boiled the " + pickling_table[int(choice)] + " thoroughly!\n")
    else:
        print("There is nothing on the pickling table to boil")


def boil(item):
    """
    function to boil items
    """
    item.disinfected = True
    print(item.describe())


def choose_to_insert():
    """
    function to choose what to insert
    """
    options = []

    table_less_jars = []
    jar = None
    if pickling_table != []:
        print("What item would you like to insert into the jar?\n")
        for item in pickling_table:
            if isinstance(item, Jar) is False:
                table_less_jars.append(item)
            else:
                jar = item
        for i in range(len(table_less_jars)):
            if isinstance(table_less_jars[i], (Cucumber)):
                print(f"" + str(i) + ". " + table_less_jars[i].__repr__())
            else:
                print(f"" + str(i) + ". " + table_less_jars[i])
        for i in range(len(table_less_jars)):
            options.append(i)

        choice = get_input(options)
        choice = int(choice)
        if choice is False:
            choose_to_insert()
        elif (choice >= 0 and choice <= len(table_less_jars)):
            print(table_less_jars[choice])
            jar.insert(table_less_jars[choice])
            print("The jar contents are as follows:")
            print(jar.contents)


def study_jar_contents():
    global current_jar
    print("The jar contains the following:")
    print(current_jar.contents)


def shake_jar():
    global current_jar
    if current_jar.lid == "on":
        current_jar.agitated = True
    elif current_jar.lid == "off":
        print("Peter Piper's pickled pepper! You forgot to put the lid back on!")
        print(f"A mix of {current_jar.contents} covers the room, and you.\n")
        current_jar.contents = []


def jar_stats():
    global current_jar
    print(current_jar.describe())


def read_cookbook():
    f = open('quick_pickling_recipe.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    f.close()



#########################################################
#########################################################
#########################################################
# Input functions

def get_input(options):
    """
    function to retrieve user input for choices
    """
    print("\n- enter a number for one of the options: ")
    choice = input("**********************************\n\n")

    validated = validate_input(choice, options)
    if validated is True:
        print("\n - A valid choice!\n")
    else:
        print("Input was invalid\n")
        return False
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
        if choiceisoption is False:
            raise ValueError(
                f"The value you entered was not one of the options given. You entered {choiceval}."
            )
    except ValueError as e:
        print(f"Invalid input: {e}, Please enter one of the numbered choices.")
        return False
    except ValueError as e:
        print(f"Invalid input: {e}, Please enter one of the numbered choices.")
        return False
    return True


#########################################################
#########################################################
#########################################################
# Run game

"""
Variables of gamestate I have in the global scope right now to get working
"""
# food items and combined ingredient arrays
garlic = "garlic"
dill = "dill"
mustard_seeds = "mustard seeds"
spices = [garlic, dill, mustard_seeds]

salt = "salt"
sugar = "sugar"
water = "water"
vinegar = "vinegar"
pickling_brine = [salt, sugar, water, vinegar]


# cutlery & crockery
spoon = "spoon"

# storage & display areas
press = [spoon, salt, sugar, water, vinegar, garlic, dill, mustard_seeds]
fridge = []
pickling_table = []
# storage_areas = [press, fridge, pickling_table]

# game_state = [storage_areas, location]

empty_jars = []
empty_jars = spawn_jars(empty_jars)
current_jar = None
current_pickle = None


populate_test_jars_fridge()
main()
