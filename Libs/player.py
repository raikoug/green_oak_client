import json

class Player():
    def __init__(self, name: str, cognome: str, soprannome: str,\
                 ex: str, pensionato: str, hobby: str, circolo: str, id,
                 fastidio = 0, scenata = False, spocchia = 0, pettegolezzo = False,
                 scenate_fatte =0, necrologio = False, parole_sagge= False, pettegolezzi = []
                 ) -> None:
        self.name = name
        self.fastidio = 0 if not fastidio else fastidio
        self.scenata = False if not scenata else scenata
        self.spocchia = 0 if not spocchia else spocchia
        self.pettegolezzo = False if not pettegolezzo else pettegolezzo
        self.scenate_fatte = 0 if not scenate_fatte else scenate_fatte
        self.necrologio = False if not necrologio else necrologio
        self.parole_sagge = False if not parole_sagge else parole_sagge
        self.pettegolezzi = list() if not pettegolezzi else pettegolezzi
        self.cognome = cognome
        self.soprannome = soprannome
        self.ex = ex
        self.pensionato = pensionato
        self.hobby = hobby
        self.circolo = circolo
        self.id = id

    def crea_pettegolezzo(self, pettegolezzo: str) -> None:
        self.pettegolezzi.append(pettegolezzo)
    
    def from_json(json_players) -> list:
        # for each player in json_players cast it to a Player object
        return [Player(
                    name =player['name'],
                    fastidio =player['fastidio'],
                    scenata =player['scenata'],
                    spocchia =player['spocchia'],
                    pettegolezzo =player['pettegolezzo'],
                    scenate_fatte =player['scenate_fatte'],
                    necrologio =player['necrologio'],
                    parole_sagge =player['parole_sagge'],
                    pettegolezzi =player['pettegolezzi'],
                    cognome =player['cognome'],
                    soprannome =player['soprannome'],
                    ex =player['ex'],
                    pensionato =player['pensionato'],
                    hobby =player['hobby'],
                    circolo =player['circolo'],
                    id =player['id'])
                       for player in json_players]

def main():
    player = Player('Giovanni', 'Cacciatore', 'Giova', 'Colombiere', 'Idraulico', 'Elettronica', 'Elettronica', 1)
    # add some random pettegolezzi
    player.crea_pettegolezzo('è risorto 3 volte')
    player.crea_pettegolezzo('Non sa contare')
    player.crea_pettegolezzo('Le infermiere sono tutte squillo')


if __name__ == '__main__':
    main()

        