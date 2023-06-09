
## Import to mantain after flattifying
#import only the methods used in this script from customtkinter
from customtkinter import CTkInputDialog, CTkFrame, CTkLabel, CTkButton, IntVar, BooleanVar, CTkCheckBox , CTkToplevel, CTkFrame, \
                          CTkButton, CTkImage, CTkFont, CTkToplevel, set_appearance_mode, set_default_color_theme, CTk

from PIL import Image
from json import loads, dumps
from os import listdir

# Import to to away after flattifying
#####################
from mazzo import Mazzo
from player import Player
#####################

COLUMNS = 19

class LastCardStats():
    spocchia = 0
    fastidio = 0
    parole_sagge = False
    necrologio = False
    scenate_fatte = 0
    pass

class command_frame(CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        row = 0

        self.title = CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        
        self.briscola = CTkButton(self, text="Briscola", command=self.master.rimoncia_pesca_briscola)
        self.pesca = CTkButton(self, text="Pesca", command=self.master.pesca)
        self.mescola = CTkButton(self, text="Mescola", command=self.master.rimoncia_pesca_briscola )
        self.crea_player = CTkButton(self, text="Crea player", command=self.master.create_player)
        self.salva_players = CTkButton(self, text="Salva", command=self.master.salva_players)

        self.title.grid(row=row, column=0, columnspan=2, padx=10, pady=(10, 0), sticky="ew")
        row += 1
        self.briscola.grid(row=row, column=0, padx=10, pady=(10, 0), sticky="ew")
        row += 1
        self.pesca.grid(row=row, column=0, padx=10, pady=(10, 0), sticky="ew")
        row += 1
        self.mescola.grid(row=row, column=0, padx=10, pady=(10, 0), sticky="ew")
        row += 1
        self.crea_player.grid(row=row, column=0, padx=10, pady=(10, 0), sticky="ew")
        row += 1
        self.salva_players.grid(row=row, column=0, padx=10, pady=(10, 0), sticky="ew")
        row += 1

class players_frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.player_row = 1
        self.players_id = {}

        self.head_name = CTkLabel(self, text="Nome")
        self.head_name.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.head_fastidio = CTkLabel(self, text="Fastidio")
        self.head_fastidio.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w", columnspan=4)

        self.head_scenata = CTkLabel(self, text="Scenata")
        self.head_scenata.grid(row=0, column=5, padx=10, pady=(10, 0), sticky="w")

        self.head_spocchia = CTkLabel(self, text="Spocchia")
        self.head_spocchia.grid(row=0, column=6, padx=10, pady=(10, 0), sticky="w", columnspan=4)

        self.head_pettegolezzo = CTkLabel(self, text="Pettegolezzo")
        self.head_pettegolezzo.grid(row=0, column=10, padx=10, pady=(10, 0), sticky="w")

        self.head_scenate_fatte = CTkLabel(self, text="Scenate fatte")
        self.head_scenate_fatte.grid(row=0, column=11, padx=10, pady=(10, 0), sticky="w", columnspan=3)

        self.head_necrologio = CTkLabel(self, text="Necrologio")
        self.head_necrologio.grid(row=0, column=14, padx=10, pady=(10, 0), sticky="w")

        self.head_parole_sagge = CTkLabel(self, text="Parole sagge")
        self.head_parole_sagge.grid(row=0, column=15, padx=10, pady=(10, 0), sticky="w")

        self.head_mostra_player_sheet = CTkLabel(self, text="Scheda")
        self.head_mostra_player_sheet.grid(row=0, column=16, padx=10, pady=(10, 0), sticky="w")

        self.head_pesca_carta = CTkLabel(self, text="Pesca")
        self.head_pesca_carta.grid(row=0, column=17, padx=10, pady=(10, 0), sticky="w")

        self.head_pennichella = CTkLabel(self, text="Pennichella")
        self.head_pennichella.grid(row=0, column=18, padx=10, pady=(10, 0), sticky="w")

    class check_box_values:
        class fastidio:
            pass
        class spocchia:
            pass
        class scenate_fatte:
            pass
        class necrologio:
            pass
        class parole_sagge:
            pass

    def add_player(self, player: Player):
        setattr(self.check_box_values.fastidio, f'{player.id}', IntVar())
        setattr(self.check_box_values.spocchia, f'{player.id}', IntVar())
        setattr(self.check_box_values.scenate_fatte, f'{player.id}', IntVar())
        setattr(self.check_box_values.necrologio, f'{player.id}', BooleanVar())
        setattr(self.check_box_values.parole_sagge, f'{player.id}', BooleanVar())
        
        fastidio_cb = getattr(self.check_box_values.fastidio, f'{player.id}')
        spocchia_cb = getattr(self.check_box_values.spocchia, f'{player.id}')
        scenate_fatte_cb = getattr(self.check_box_values.scenate_fatte, f'{player.id}')
        necrologio_cb = getattr(self.check_box_values.necrologio, f'{player.id}')
        parole_sagge_cb = getattr(self.check_box_values.parole_sagge, f'{player.id}')


        self.name = CTkLabel(self, text=player.name)
        self.players_id[player.id] = dict()

        # 4 checkbox Fastidio
        self.name.grid(row=self.player_row, column=0, padx=10, pady=(10, 0), sticky="w")



        self.players_id[player.id]['fastidio_1'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=1  , offvalue=0)
        self.players_id[player.id]['fastidio_1'].grid(row=self.player_row, column=1, padx=0, pady=0, sticky="w")

        self.players_id[player.id]['fastidio_2'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=2  , offvalue=-1)
        self.players_id[player.id]['fastidio_2'].grid(row=self.player_row, column=2, padx=0, pady=0, sticky="w")

        self.players_id[player.id]['fastidio_3'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=3  , offvalue=-2)
        self.players_id[player.id]['fastidio_3'].grid(row=self.player_row, column=3, padx=0, pady=0, sticky="w")

        self.players_id[player.id]['fastidio_4'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=4  , offvalue=-3)
        self.players_id[player.id]['fastidio_4'].grid(row=self.player_row, column=4, padx=0, pady=0, sticky="w")

        # 1 CTkCheckBox Scenata
        self.players_id[player.id]['scenata'] = CTkButton(self, text="Scenata!", width=10, command=lambda: self.master.scenata(player))
        self.players_id[player.id]['scenata'].grid(row=self.player_row, column=5, padx=15, pady=0, sticky="w")

        # 4 CTkCheckBox Spocchia
        self.players_id[player.id]['spocchia_1'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=1  , offvalue=0)
        self.players_id[player.id]['spocchia_1'].grid(row=self.player_row, column=6, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['spocchia_2'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=2  , offvalue=-1)
        self.players_id[player.id]['spocchia_2'].grid(row=self.player_row, column=7, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['spocchia_3'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=3  , offvalue=-2)
        self.players_id[player.id]['spocchia_3'].grid(row=self.player_row, column=8, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['spocchia_4'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=4  , offvalue=-3)
        self.players_id[player.id]['spocchia_4'].grid(row=self.player_row, column=9, padx=0, pady=0, sticky="w")

        # 1 CTkCheckBox Pettegolezzo
        self.players_id[player.id]['pettegolezzo'] = CTkButton(self, text="Pettegolezzo", width=10, command=lambda: self.master.pettegolezzo(player)) 
        self.players_id[player.id]['pettegolezzo'].grid(row=self.player_row, column=10, padx=15, pady=0, sticky="w")

        # 3 CTkCheckBox Scenate fatte
        self.players_id[player.id]['scenate_fatte_1'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "scenate_fatte"), 
                                                                             variable=scenate_fatte_cb, onvalue=1  , offvalue=0)
        self.players_id[player.id]['scenate_fatte_1'].grid(row=self.player_row, column=11, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['scenate_fatte_2'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "scenate_fatte"), 
                                                                             variable=scenate_fatte_cb, onvalue=2  , offvalue=-1)
        self.players_id[player.id]['scenate_fatte_2'].grid(row=self.player_row, column=12, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['scenate_fatte_3'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "scenate_fatte"), 
                                                                             variable=scenate_fatte_cb, onvalue=3  , offvalue=-2)
        self.players_id[player.id]['scenate_fatte_3'].grid(row=self.player_row, column=13, padx=0, pady=0, sticky="w")

        # 1 CTkCheckBox Necrologio
        self.players_id[player.id]['necrologio'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "necrologio"), 
                                                                             variable=necrologio_cb, onvalue=True  , offvalue=False)
        self.players_id[player.id]['necrologio'].grid(row=self.player_row, column=14, padx=15, pady=0, sticky="w")

        # 1 CTkCheckBox Parole sagge
        self.players_id[player.id]['parole_sagge'] = CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "parole_sagge"), 
                                                                             variable=parole_sagge_cb, onvalue=True  , offvalue=False)
        self.players_id[player.id]['parole_sagge'].grid(row=self.player_row, column=15, padx=15, pady=0, sticky="w")

        # 1 CTkCheckBox Mostra scheda
        self.players_id[player.id]['mostra_player_sheet'] = CTkButton(self, text="Scheda", width=10 , command=lambda: self.master.show_player_sheet(player))
        self.players_id[player.id]['mostra_player_sheet'].grid(row=self.player_row, column=16, padx=15, pady=0, sticky="w")

        # 1 CTkButton per pescare una carta
        self.players_id[player.id]['pesca_carta'] = CTkButton(self, text="Pesca", width=10, command=lambda: self.master.pesca(player))
        self.players_id[player.id]['pesca_carta'].grid(row=self.player_row, column=17, padx=15, pady=0, sticky="w")

        self.players_id[player.id]['pennichella'] = CTkButton(self, text="Pennichella", width=10, command=lambda: self.master.pennichella(player))
        self.players_id[player.id]['pennichella'].grid(row=self.player_row, column=18, padx=15, pady=0, sticky="w")

        
        self.player_row += 1

    def update_playerid_stats(self, player):
        fastidio = self.master.last_card_stats.fastidio + player.fastidio

        player.fastidio = min(4, fastidio)

        if player.fastidio == 4:
            self.players_id[player.id]['fastidio_1'].select()
            self.players_id[player.id]['fastidio_2'].select()
            self.players_id[player.id]['fastidio_3'].select()
            self.players_id[player.id]['fastidio_4'].select()
        elif player.fastidio == 3:
            self.players_id[player.id]['fastidio_1'].select()
            self.players_id[player.id]['fastidio_2'].select()
            self.players_id[player.id]['fastidio_3'].select()
            self.players_id[player.id]['fastidio_4'].deselect()
        elif player.fastidio == 2:
            self.players_id[player.id]['fastidio_1'].select()
            self.players_id[player.id]['fastidio_2'].select()
            self.players_id[player.id]['fastidio_3'].deselect()
            self.players_id[player.id]['fastidio_4'].deselect()
        elif player.fastidio == 1:
            self.players_id[player.id]['fastidio_1'].select()
            self.players_id[player.id]['fastidio_2'].deselect()
            self.players_id[player.id]['fastidio_3'].deselect()
            self.players_id[player.id]['fastidio_4'].deselect()
        elif player.fastidio == 0:
            self.players_id[player.id]['fastidio_1'].deselect()
            self.players_id[player.id]['fastidio_2'].deselect()
            self.players_id[player.id]['fastidio_3'].deselect()
            self.players_id[player.id]['fastidio_4'].deselect()
        
        spocchia = self.master.last_card_stats.spocchia + player.spocchia
        player.spocchia = min(4, spocchia)

        if player.spocchia == 4:
            self.players_id[player.id]['spocchia_1'].select()
            self.players_id[player.id]['spocchia_2'].select()
            self.players_id[player.id]['spocchia_3'].select()
            self.players_id[player.id]['spocchia_4'].select()
        elif player.spocchia == 3:
            self.players_id[player.id]['spocchia_1'].select()
            self.players_id[player.id]['spocchia_2'].select()
            self.players_id[player.id]['spocchia_3'].select()
            self.players_id[player.id]['spocchia_4'].deselect()
        elif player.spocchia == 2:
            self.players_id[player.id]['spocchia_1'].select()
            self.players_id[player.id]['spocchia_2'].select()
            self.players_id[player.id]['spocchia_3'].deselect()
            self.players_id[player.id]['spocchia_4'].deselect()
        elif player.spocchia == 1:
            self.players_id[player.id]['spocchia_1'].select()
            self.players_id[player.id]['spocchia_2'].deselect()
            self.players_id[player.id]['spocchia_3'].deselect()
            self.players_id[player.id]['spocchia_4'].deselect()
        elif player.spocchia == 0:
            self.players_id[player.id]['spocchia_1'].deselect()
            self.players_id[player.id]['spocchia_2'].deselect()
            self.players_id[player.id]['spocchia_3'].deselect()
            self.players_id[player.id]['spocchia_4'].deselect()
        
        if not player.parole_sagge:
            parole_sagge = self.master.last_card_stats.parole_sagge
            if parole_sagge:
                player.parole_sagge = True
                self.players_id[player.id]['parole_sagge'].select()
        
        if not player.necrologio:
            necrologio = self.master.last_card_stats.necrologio
            if necrologio:
                player.necrologio = True
                self.players_id[player.id]['necrologio'].select()

        player.scenate_fatte = min(3, self.master.last_card_stats.scenate_fatte + player.scenate_fatte)

        if player.scenate_fatte == 3:
            self.players_id[player.id]['scenate_fatte_1'].select()
            self.players_id[player.id]['scenate_fatte_2'].select()
            self.players_id[player.id]['scenate_fatte_3'].select()
        elif player.scenate_fatte == 2:
            self.players_id[player.id]['scenate_fatte_1'].select()
            self.players_id[player.id]['scenate_fatte_2'].select()
            self.players_id[player.id]['scenate_fatte_3'].deselect()
        elif player.scenate_fatte == 1:
            self.players_id[player.id]['scenate_fatte_1'].select()
            self.players_id[player.id]['scenate_fatte_2'].deselect()
            self.players_id[player.id]['scenate_fatte_3'].deselect()
        elif player.scenate_fatte == 0:
            self.players_id[player.id]['scenate_fatte_1'].deselect()
            self.players_id[player.id]['scenate_fatte_2'].deselect()
            self.players_id[player.id]['scenate_fatte_3'].deselect()
            

class card_frame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        #crea a frame on the left to show the briscola card
        self.briscola_frame = CTkFrame(self)
        self.briscola_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        
        # init gird for self.briscola_frame
        self.briscola_frame.grid_columnconfigure(0, weight=1)
        self.briscola_frame.grid_rowconfigure(0, weight=1)
        
        
        self.show_briscola_card()

        #crea a frame on the right to show the cards of the player
        self.player_frame = CTkFrame(self)
        self.player_frame.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        self.player_frame.grid_columnconfigure(0, weight=1)
        self.player_frame.grid_rowconfigure(0, weight=1)

        self.show_player_cards(self.master.mazzo.last_card)

        # crea un fram con le informazioni sulla carta pescata
        self.info_frame = CTkFrame(self)
        self.info_frame.grid(row=0, column=2, sticky="ew", padx=10, pady=10)
        self.info_frame.grid_columnconfigure(0, weight=1)
        self.info_frame.grid_rowconfigure(0, weight=1)

        self.show_info_card(self.master.mazzo.last_card)

        # crea un frame dove metterò il numero di carte del mazzo rimaste
        self.mazzo_frame = CTkFrame(self)
        self.mazzo_frame.grid(row=1, column=0, sticky="ns", padx=5, pady=5, columnspan=3)

        self.mazzo_frame.grid_columnconfigure(0, weight=1)
        self.mazzo_frame.grid_rowconfigure(0, weight=1)


        self.show_info_mazzo()

    def show_info_mazzo(self):
        # remove all widgets from the frame
        for widget in self.mazzo_frame.winfo_children():
            widget.destroy()

        # crea un label con il numero di carte rimaste nel mazzo
        mazzo_label = CTkLabel(self.mazzo_frame, text=f"Carte ancora nel mazzo: {self.master.mazzo.carte_rimaste()}",
                                             font = self.master.my_font_description, text_color='cyan')
        mazzo_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    
    def show_info_card(self, card):
        # remove all widgets from the frame
        for widget in self.info_frame.winfo_children():
            widget.destroy()


        # laber with card name
        i = 0
        card_name = CTkLabel(self.info_frame, text=card.name)
        card_name.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
        i += 1
        if card.seme == self.master.briscola.seme:
            # show a CTkLabel in Dark Green saying the card is of Briscola
            briscola_label = CTkLabel(self.info_frame, text="Briscola", text_color="green" )
            briscola_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1
            successo = CTkLabel(self.info_frame, text="Successo", text_color="green")
            successo.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1
            
            if card.value in [2, 4, 5, 6 ,7]:
                spocchia_label = CTkLabel(self.info_frame, text="Spocchia (2)", )
                self.master.last_card_stats.spocchia = 2
                spocchia_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value in [8, 9, 10]:
                spocchia_label = CTkLabel(self.info_frame, text="Spocchia (2/3)", )
                self.master.last_card_stats.spocchia = 2
                spocchia_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value == 3:
                spocchia_label = CTkLabel(self.info_frame, text="Spocchia (4)", )
                self.master.last_card_stats.spocchia = 4
                spocchia_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                parole_sagge = CTkLabel(self.info_frame, text="Parfole Sagge", )
                self.master.last_card_stats.parole_sagge = True
                parole_sagge.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            else:
                pettegolezzo = CTkLabel(self.info_frame, text="Pettegolezzo", )
                pettegolezzo.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                cambia_briscola = CTkLabel(self.info_frame, text="Cambia Briscola", )
                cambia_briscola.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1

        else:
            # show a CTkLabel in Dark Red saying the card is not of Briscola
            briscola_label = CTkLabel(self.info_frame, text="Non Briscola", text_color="red")
            briscola_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1
            
            fallimento = CTkLabel(self.info_frame, text="Fallimento", text_color="Red")
            fallimento.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1

            if card.value in [2, 4, 5, 6 ,7]:
                fastidio = CTkLabel(self.info_frame, text="Fastidio (1)", )
                self.master.last_card_stats.fastidio = 1
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                lamentela = CTkLabel(self.info_frame, text="Lamentela", )
                lamentela.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value in [8, 9, 10]:
                fastidio = CTkLabel(self.info_frame, text="Fastidio (2)", )
                self.master.last_card_stats.fastidio = 2
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                lamentela = CTkLabel(self.info_frame, text="Lamentela", )
                lamentela.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value == 3:
                fastidio = CTkLabel(self.info_frame, text="Fastidio (3)", )
                self.master.last_card_stats.fastidio = 3
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                sproloquio = CTkLabel(self.info_frame, text="Sproloquio", )
                sproloquio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            else:
                fastidio = CTkLabel(self.info_frame, text="Fastidio (4)", )
                self.master.last_card_stats.fastidio = 4
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                necrologio = CTkLabel(self.info_frame, text="Necrologio", )
                self.master.last_card_stats.necrologio = True
                necrologio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1

    def show_briscola_card(self):    
        my_image = CTkImage(light_image=Image.open(self.master.briscola.path),
                                  dark_image=Image.open(self.master.briscola.path),
                                  size=(177, 285))
        image_label = CTkLabel(self.briscola_frame, image=my_image, text="")
        image_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def show_player_cards(self, card):
        my_image = CTkImage(light_image=Image.open(card.path),
                                  dark_image=Image.open(card.path),
                                  size=(177, 285))
        image_label = CTkLabel(self.player_frame, image=my_image, text="")
        image_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

class Gui(CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.mazzo = Mazzo()
        self.last_card_stats = LastCardStats()
        self.mazzo.pesca()
        self.briscola = self.mazzo.last_card
        self.mazzo.pesca()

        self.my_font_bold = CTkFont(family="Helvetica", size=13, weight="bold")

        # create some fonts for titles, description, bad things and good things
        self.my_font_title = CTkFont(family="Helvetica", size=15, weight="bold")
        self.my_font_description = CTkFont(family="Helvetica", size=13, weight="bold")
        self.my_font_bad = CTkFont(family="Helvetica", size=13, weight="bold")
        self.my_font_good = CTkFont(family="Helvetica", size=13, weight="bold")



        set_appearance_mode("System")  # Modes: system (default), light, dark
        set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        #self.title = "Green Oaks"
        self.geometry("1300x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # TopLevel windows init
        self.custom_dialog_window = None
        self.toplevel_window = None


        self.command_frame = command_frame(self, "Comandi")
        self.command_frame.grid(row=0, column=COLUMNS, sticky="nsew", rowspan=2, pady=10, padx=10)
        
        self.player_frame = players_frame(self)
        self.player_frame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10, columnspan=COLUMNS)

        self.load_players()
        
        
        self.card_frame = card_frame(self)
        self.card_frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=10, columnspan=COLUMNS-1)
   
    def load_players(self):
        if "players.json" in listdir():
            json_players = loads(open("players.json", "r").read())
            self.players = Player.from_json(json_players)

            for player in self.players:
                self.player_frame.add_player(player)
                self.last_card_stats = LastCardStats()
                self.player_frame.update_playerid_stats(player)
        else:
            self.players = list()
    
    def create_player(self) -> None:
        player_id = len(self.players) + 1
        # Get Player Nome
        dialog = CTkInputDialog(text="Nome Player:", title="Nome Player")
        nome = dialog.get_input()  # waits for input

        # Get Player Cognome
        dialog = CTkInputDialog(text="Cognome Player:", title="Cognome Player")
        cognome = dialog.get_input()  # waits for input

        # Get Player Soprannome
        dialog = CTkInputDialog(text="Soprannome Player:", title="Soprannome Player")
        soprannome = dialog.get_input()  # waits for input

        # Get Player Ex
        dialog = CTkInputDialog(text="Ex Professione:", title="Ex Professione")
        ex = dialog.get_input()  # waits for input

        # Get Player Pensionato
        dialog = CTkInputDialog(text="Pensionamento:", title="Pensionamento")
        pensionato = dialog.get_input()  # waits for input

        # Get Player Hobby
        dialog = CTkInputDialog(text="Hobby:", title="Hobby")
        hobby = dialog.get_input()  # waits for input

        # Get Player Circolo
        dialog = CTkInputDialog(text="Circolo:", title="Circolo")
        circolo = dialog.get_input()  # waits for input

        self.add_player(Player(nome, cognome, soprannome, ex, pensionato, hobby, circolo, player_id))

    def add_player(self, player: Player) -> None:
        self.players.append(player)
        self.player_frame.add_player(player)

    def show_player_sheet(self, player: Player):
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = PlayerSheet(player, self)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it

    def rimoncia_pesca_briscola(self):
        self.mazzo.ricomincia()
        self.mazzo.pesca()
        self.briscola = self.mazzo.last_card
        self.card_frame.show_briscola_card()
        self.card_frame.show_info_mazzo()

    def pesca(self, player=None):
        self.mazzo.pesca()
        self.last_card_stats = LastCardStats()
        self.card_frame.show_player_cards(self.mazzo.last_card)
        self.card_frame.show_info_card(self.mazzo.last_card)
        
        if player is not None:
            self.player_frame.update_playerid_stats(player)
        
        self.card_frame.show_info_mazzo()
    
    def scenata(self, player: Player):
        if player.scenate_fatte == 3:
            self.show_dialog("Scenate finite", "Non puoi fare scenate! Vai a nanna!")
        elif not player.fastidio == 4:
            self.show_dialog("Scenate finite", "Non puoi fare scenate, Non ti hanno ancora infastidito abbstanza!")
        else:
            player.fastidio = 0
            player.scenate_fatte += 1
            self.last_card_stats = LastCardStats()
            self.last_card_stats.fastidio = -(player.fastidio)
            self.player_frame.update_playerid_stats(player)

    def pettegolezzo(self, player: Player):
        if not player.spocchia == 4:
            self.show_dialog("Pettegolezzi finiti", "Non puoi fare pettegolezzi, non hai ancora accumlato abbstanza spocchia!")
        else:
            player.spocchia = 0
            self.last_card_stats = LastCardStats()
            self.last_card_stats.spocchia = -(player.spocchia)
            self.player_frame.update_playerid_stats(player)
            pettegolezzo = CTkInputDialog(text="Hai dirtto a creare un nuovo pettegolezzo:", title="Pettegolezzo")
            player.crea_pettegolezzo(pettegolezzo.get_input())

    def pennichella(self, player: Player):
        if player.scenate_fatte == 3:
            player.fastidio = 0
            player.scenate_fatte = 0
            self.last_card_stats = LastCardStats()
            self.last_card_stats.fastidio = -(player.fastidio)
            self.last_card_stats.scenate_fatte = -(player.scenate_fatte)
            self.player_frame.update_playerid_stats(player)
        else:
            self.show_dialog("Scenate Insufficienti", "Non puoi fare la pennichella, non hai fatto abbastanza scenate!")

    def checkbox_toggle(self, player: Player, stat: str):
        stat_box = getattr(self.player_frame.check_box_values, stat)
        value = getattr(stat_box, f'{player.id}').get()
        if stat in ["fastidio", "spocchia", "scenate_fatte"]:
            # va messo fastidio al valore ottenuto, quando positivo. quando negativo non ne ho idea.
            if value > 0 :
                #checkbox selezionato
                self.last_card_stats = LastCardStats()
                setattr(self.last_card_stats, stat, 0)
                setattr(player, stat, value)
                self.player_frame.update_playerid_stats(player)
            else:
                # checkbox deselzionato
                self.last_card_stats = LastCardStats()
                setattr(self.last_card_stats, stat, 0)
                setattr(player, stat, -value)
                self.player_frame.update_playerid_stats(player)

        else: # "parole_sagge", "necrologio"
            if value: 
                self.last_card_stats = LastCardStats()
                setattr(self.last_card_stats, stat, True)
                setattr(player, stat, False)
                self.player_frame.update_playerid_stats(player)
            else:
                self.last_card_stats = LastCardStats()
                setattr(self.last_card_stats, stat, False)
                setattr(player, stat, False)
                self.player_frame.update_playerid_stats(player)        

    def salva_players(self):
        json_players = [player.__dict__ for player in self.players]
        open('players.json', 'w').write(dumps(json_players, indent=2))
        self.show_dialog("Salvataggio avvenuto con successo!", "Salvato!")

    def show_dialog(self, title, text):
        if self.custom_dialog_window is None or not self.custom_dialog_window.winfo_exists():
            self.custom_dialog_window = Custom_Dialog(title, text, self) 
        else:
            self.custom_dialog_window.focus()  # if window exists focus it

class Custom_Dialog(CTkToplevel):
    def __init__(self, title, text, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        altezza = 100
        larghezza = len(text) * 7

        self.geometry(f"{larghezza}x{altezza}")
        self.title(title)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = CTkLabel(self, text=text)
        self.label.pack(padx=20, pady=20)

class PlayerSheet(CTkToplevel):
    def __init__(self, player, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
        self.geometry("700x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)


        COLUMNS = 2

        name = player.name
        fastidio = player.fastidio
        scenata = "Sì" if player.scenata else "No"
        spocchia = player.spocchia
        pettegolezzi = player.pettegolezzo
        scenate_fatte = player.scenate_fatte
        necrologio = "Sì" if player.necrologio else "No"
        parole_sagge = "Sì" if player.parole_sagge else "No"
        pettegolezzi = player.pettegolezzi
        cognome = player.cognome
        soprannome = player.soprannome
        ex = player.ex
        pensionato = player.pensionato
        hobby = player.hobby
        circolo = player.circolo
        id = player.id
        
        self.title(f"Scheda di {name} {cognome}")

        self.top_frame = CTkFrame(master = self)
        self.top_frame.grid(row=0, column=0, sticky="ew", padx=5, pady= 5, columnspan=COLUMNS)

        self.top_frame_titolo = CTkLabel(master=self.top_frame, text=f"{name} {cognome}, ex {ex}, {pensionato} in pensione, con l'hobby del {hobby}",
                                              font = self.master.my_font_title, text_color="purple")

        self.top_frame_titolo.grid(row=0, column=0, sticky="ew", padx=5, pady= 5, columnspan=COLUMNS)
        

        self.fastidio_spocchia = CTkFrame(master=self)
        self.fastidio_spocchia.grid(row=1, column=0, sticky="ew", padx=5, pady= 5)
        fastidio_spocchia_i = 0

        self.fastidio_spocchia_titolo = CTkLabel(master=self.fastidio_spocchia, text="Fastidio e Spocchia", font = self.master.my_font_title, text_color="cyan")
        self.fastidio_spocchia_titolo.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
        fastidio_spocchia_i += 1

        self.fastidio_spocchia_fastidio = CTkLabel(master=self.fastidio_spocchia, text=f"Fastidio: {fastidio}", font = self.master.my_font_description , text_color="white")
        self.fastidio_spocchia_fastidio.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
        fastidio_spocchia_i += 1

        if fastidio == 4:
            self.fastidio_spocchia_scenata_fatta = CTkLabel(master=self.fastidio_spocchia, text=f"Scenata fatta?: {scenata}", font = self.master.my_font_description , text_color="white")
            self.fastidio_spocchia_scenata_fatta.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
            fastidio_spocchia_i += 1

        self.fastidio_spocchia_spocchia = CTkLabel(master=self.fastidio_spocchia, text=f"Spocchia: {spocchia}", font = self.master.my_font_description , text_color="white")
        self.fastidio_spocchia_spocchia.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
        fastidio_spocchia_i += 1


        self.fastidio_spocchia_scenate_fatte = CTkLabel(master=self.fastidio_spocchia, text=f"Spocchia: {scenate_fatte}", font = self.master.my_font_description , text_color="white")
        self.fastidio_spocchia_scenate_fatte.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
        fastidio_spocchia_i += 1

        self.fastidio_spocchia_necrologio = CTkLabel(master=self.fastidio_spocchia, text=f"Necrologio: {necrologio}", font = self.master.my_font_description , text_color="white")
        self.fastidio_spocchia_necrologio.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
        fastidio_spocchia_i += 1

        self.fastidio_spocchia_parole_sagge = CTkLabel(master=self.fastidio_spocchia, text=f"Parole Sagge: {parole_sagge}", font = self.master.my_font_description , text_color="white")
        self.fastidio_spocchia_parole_sagge.grid(row=fastidio_spocchia_i, column=0, sticky="ew", columnspan=COLUMNS)
        fastidio_spocchia_i += 1

        
        self.player_info_frame = CTkFrame(master=self)
        self.player_info_frame.grid(row=1, column=1, sticky="ew", padx=5, pady= 5)

        self.player_info_frame_titolo = CTkLabel(master=self.player_info_frame, text="Info Personali", font = self.master.my_font_title, text_color="cyan")
        self.player_info_frame_titolo.grid(row=0, column=0, sticky="ew", columnspan=COLUMNS)

        self.player_info_frame_nome = CTkLabel(master=self.player_info_frame, text=f"Nome: {name}", font = self.master.my_font_description , text_color="white")
        self.player_info_frame_nome.grid(row=1, column=0, sticky="ew", columnspan=COLUMNS)

        self.player_info_frame_cognome = CTkLabel(master=self.player_info_frame, text=f"Cognome: {cognome}", font = self.master.my_font_description , text_color="white")
        self.player_info_frame_cognome.grid(row=2, column=0, sticky="ew", columnspan=COLUMNS)

        self.player_info_frame_soprannome = CTkLabel(master=self.player_info_frame, text=f"Soprannome: {soprannome}", font = self.master.my_font_description , text_color="white")
        self.player_info_frame_soprannome.grid(row=3, column=0, sticky="ew", columnspan=COLUMNS)

        self.player_info_frame_circolo = CTkLabel(master=self.player_info_frame, text=f"Circolo: {circolo}", font = self.master.my_font_description , text_color="white")
        self.player_info_frame_circolo.grid(row=4, column=0, sticky="ew", columnspan=COLUMNS)

        self.pettegolezzi_frame = CTkFrame(master=self)
        self.pettegolezzi_frame.grid(row=2, column=0, sticky="ew", padx=5, pady= 5, columnspan=COLUMNS)

        self.pttegolezzi_titolo = CTkLabel(master=self.pettegolezzi_frame, text="Pettegolezzi", font = self.master.my_font_title, text_color="cyan")
        self.pttegolezzi_titolo.grid(row=0, column=0, sticky="ew", padx=5, pady= 5, columnspan=COLUMNS)

        for i, pettegolezzo in enumerate(pettegolezzi):
            self.pettegolezzi_frame_pettegolezzo = CTkLabel(master=self.pettegolezzi_frame, text=f"{pettegolezzo}", font = self.master.my_font_description , text_color="white")
            self.pettegolezzi_frame_pettegolezzo.grid(row=i+1, column=0, sticky="ew", padx=5, pady= 5, columnspan=COLUMNS)









if __name__ == "__main__":
    app = Gui()
    app.mainloop()



    