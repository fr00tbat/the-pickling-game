
fridge = [[],[],[]]
pickling_table = []


class Jar:
    """jar class"""
    def __init__(self):
        # properties
        self.size = "medium"
        self.label = ""
        self.contents = []
        self.lid = "on"

    def describe(self):
        return f"description: \nsize: {self.size}\nlabel: {self.label}\ncontents: {self.contents}\nlid: {self.lid}"

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
        return f"description: \npickledness: {self.pickledeness}\ncrunch: {self.crunch}"


cucumber1 = Cucumber()
print(cucumber1.describe())

