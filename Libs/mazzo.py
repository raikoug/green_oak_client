
# Import to matain after flattifying
from random import choice
from json import loads

# Import to to away after flattifying
#####################
from cards import Card
#####################


class Mazzo():
    cards = [ Card(carta['seme'], carta['value'], carta['path']) for carta in loads(open("./Assets/carte.json", "r").read())]

    
    def __init__(self):
        self.cards = list([ Card(carta['seme'], carta['value'], carta['path']) for carta in loads(open("./Assets/carte.json", "r").read())])
    
    def pesca(self) -> None:
        card = choice([ carta for carta in self.cards if not carta.pescata])
        if len(self.cards) == 0:
            self.ricomincia()
        
        card.pescata = True
        self.last_card = card


    def ricomincia(self) -> None:
        self.__init__()
    
    def __str__(self) -> str:
        return f'Carte rimaste nel mazzo: {len(self.cards)}'
    
    def __repr__(self) -> str:
        return f'Carte rimaste nel mazzo: {len(self.cards)}'
    
    def print(self) -> None:
        for card in self.cards:
            print(card)

    def carte_rimaste(self) -> int:
        return len([card for card in self.cards if not card.pescata ])
    

def main():
    mazzo = Mazzo()
    mazzo.pesca()
    print(mazzo.last_card)
    print(mazzo)
    mazzo.print()
    print(mazzo.carte_rimaste())
    mazzo.pesca()
    print(mazzo.carte_rimaste())
    mazzo.ricomincia()
    print(mazzo.carte_rimaste())

if __name__ == '__main__':
    main()
