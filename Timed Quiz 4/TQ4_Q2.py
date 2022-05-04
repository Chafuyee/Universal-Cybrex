
class PlayingCard:

    def __init__(self, item) -> None:
        self.card = item

    def value(self):
        card_list = ["T", "J", "Q", "K"]
        if self.card[0] == "A":
            return 11
        elif self.card[0] in card_list:
            return 10
        else: 
            return self.card[0]

    def __str__(self):
        return (self.card)

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []

    def points(self):
        total_points = 0
        special_list = ["T", "J", "Q", "K"]
        for card in self.cards:
            if card[0] == "A":
                total_points += 11
            elif card[0] in special_list:
                total_points += 10
            else:
                card_num = int(card[0])
                total_points += card_num
        return total_points
            
    
    def add(self, card):
        self.cards += [card]
        

    def __str__(self) -> str:
        cards_string = ''
        for card in self.cards:
            cards_string += str(card) + ' '
        return self.name + ': ' + cards_string
