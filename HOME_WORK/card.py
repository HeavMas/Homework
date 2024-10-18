class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_suit(self):
        print(self.suit)
    def get_value(self):
        print(self.value)

if __name__ == '__main__':
    card = Card("Clubs", 10)
    card.get_suit()
    card.get_value()