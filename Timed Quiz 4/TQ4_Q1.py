
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

a_card = PlayingCard('2S')
print(a_card.value())