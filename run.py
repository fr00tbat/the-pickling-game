
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


jar1 = Jar()
print(jar1.describe())





