#A framework for an inventory system, could go one step further and define 
#A class for items but for now items will just be strings.
class Inventory(object):
    def __init__(self):
        self.content = []
    def pickup(self, item):
        self.content.append(item)
    def drop(self, item):
        self.content.remove(item)
    def holding(self, item):
        return item in self.content

items = Inventory()    
