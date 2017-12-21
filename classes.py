races = []

class Race:

    resident_country = 'Hungary'
    category = 'c1'

    def __init__(self, name, type='cx'):
        # self = this. This is good so from now I can reference to the name property of the race object from anywhere in the class
        self.name = name
        self.type = type
        #self.category = self.category
        races.append(self)
        print(races)

    # this is just have a friendly name when I printing the object itself
    def __str__(self):
        return 'Race ' + self.name

    # I can reference to the name property of the object and capitalize its name
    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_country(self):
        return self.resident_country


# this is going to inherit all methods from the parent class so I can use them
class AmatureRace(Race):
    resident_country = 'Hungary'
    category = 'c2'

miskolc = AmatureRace('miskolc')
crossliget = Race('crossliget')
#print(miskolc.get_name_capitalize())
#print(races)
