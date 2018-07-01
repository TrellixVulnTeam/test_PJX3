from race import Race
# this is going to inherit all methods from the parent class so I can use them
class AmatureRace(Race):
    resident_country = 'Hungary'
    category = 'c2'

    def get_category(self):
        return super().get_category()

    def get_name_capitalize(self):
        original = super().get_name_capitalize()
        return  original + '-HS'

