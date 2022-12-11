class Hero():
    def __init__(self, power, name, rank):
        self.powr = power
        self.name = name
        self.__rank = rank
    def getrank(self):
        print('Твой ранг ->', self.__rank)
    def setrank(self):
        self.__rank = 'Победитель арены'
        print('Теперь вы', self.__rank)
    def delrank(self):
        del self.__rank