from cards import Card
from random import choice
import json

class Mazzo():
    cards = [ Card(carta['seme'], carta['value'], carta['path']) for carta in json.loads(open("./Assets/carte.json", "r").read())]

    
    def __init__(self):
        self.cards = Mazzo.cards
    
    def pesca(self) -> None:
        card = choice([ carta for carta in self.cards if not carta.pescata])
        if len(self.cards) == 0:
            self.ricomincia()
        
        card.pescata = True
        self.last_card = card


    def ricomincia(self) -> None:
        del self.cards
        self.cards = Mazzo.cards
    
    def __str__(self) -> str:
        return f'Carte rimaste nel mazzo: {len(self.cards)}'
    
    def __repr__(self) -> str:
        return f'Carte rimaste nel mazzo: {len(self.cards)}'
    
    def print(self) -> None:
        for card in self.cards:
            print(card)

def main():
    mazzo = Mazzo()
    mazzo.pesca()
    print(mazzo.last_card)
    print(mazzo)
    mazzo.print()

if __name__ == '__main__':
    main()
