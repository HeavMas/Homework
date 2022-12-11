class SObject():
    def __init__(self, size):
        self.size = size
class Star(SObject):
    def __init__(self, size, bright):
        super().__init__(size)
        self.bright = bright
    def brightness(self, bright):
        print('Звезда светит с яркостью ->' + str(bright))
class Planet(SObject):
    def __init__(self, size, populathion, years):
        super().__init__(size)
        self.populathion = populathion
        self.years = years
    def pop(self, populathion, years):
        print('Через',  str(years),  'лет на планете будет', populathion * years, 'человек')
