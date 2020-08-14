allset = []
items = []

def append_set(self, bsk):
    self.set.append(bsk)

def add_items():
    for bsk in allset:
        create_item(allset[bsk])

class i_bsk(object):
    def __init__(self, name):
        self.name = name
        self.bsk = None
        self.no_items = None
        allset.append(self)

    def add_bsk(self, string):
        basket = string.rstrip("\n")
        self.bsk = basket.split(", ")


class item(object):
    def __init__(self):
        self.name = self
        self.confidence = None
        self.support = None


def create_item(bsk):
    for item in bsk:
        if bsk[item] not in items:
            items.append(item)

