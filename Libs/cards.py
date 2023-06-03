
class Card():
    def __init__(self, seme, value, path):
        self.seme = seme
        self.value = value
        self.path = path
        self.name = f'{self.value} of {self.seme}'
        self.pescata = False

    def __str__(self):
        return f'{self.value} di {self.seme}'

    def __repr__(self):
        return f'{self.value} di {self.seme}'
    

def main():
    card = Card('cuori', '2', './Assets/2_of_hearts.png')
    print(card)
    print(card.name)
    print(card.pescata)
    card.pescata = True
    print(card.pescata)
    print(card.path)
    print(card)

if __name__ == '__main__':
    main()
    