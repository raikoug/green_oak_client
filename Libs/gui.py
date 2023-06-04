import customtkinter
from player import Player
from PIL import Image
import json
from cards import Card
from mazzo import Mazzo
from os import listdir

COLUMNS = 19

class LastCardStats():
    spocchia = 0
    fastidio = 0
    parole_sagge = False
    necrologio = False
    scenate_fatte = 0
    pass

class command_frame(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        row = 0

        self.title = customtkinter.CTkLabel(self, text=title, fg_color="gray30", corner_radius=6)
        
        self.briscola = customtkinter.CTkButton(self, text="Briscola", command=self.master.rimoncia_pesca_briscola)
        self.pesca = customtkinter.CTkButton(self, text="Pesca", command=self.master.pesca)
        self.mescola = customtkinter.CTkButton(self, text="Mescola", command=self.master.rimoncia_pesca_briscola )
        self.crea_player = customtkinter.CTkButton(self, text="Crea player", command=self.master.create_player)
        self.salva_players = customtkinter.CTkButton(self, text="Salva", command=self.master.salva_players)

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


class players_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.player_row = 1
        self.players_id = {}

        self.head_name = customtkinter.CTkLabel(self, text="Nome")
        self.head_name.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        self.head_fastidio = customtkinter.CTkLabel(self, text="Fastidio")
        self.head_fastidio.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w", columnspan=4)

        self.head_scenata = customtkinter.CTkLabel(self, text="Scenata")
        self.head_scenata.grid(row=0, column=5, padx=10, pady=(10, 0), sticky="w")

        self.head_spocchia = customtkinter.CTkLabel(self, text="Spocchia")
        self.head_spocchia.grid(row=0, column=6, padx=10, pady=(10, 0), sticky="w", columnspan=4)

        self.head_pettegolezzo = customtkinter.CTkLabel(self, text="Pettegolezzo")
        self.head_pettegolezzo.grid(row=0, column=10, padx=10, pady=(10, 0), sticky="w")

        self.head_scenate_fatte = customtkinter.CTkLabel(self, text="Scenate fatte")
        self.head_scenate_fatte.grid(row=0, column=11, padx=10, pady=(10, 0), sticky="w", columnspan=3)

        self.head_necrologio = customtkinter.CTkLabel(self, text="Necrologio")
        self.head_necrologio.grid(row=0, column=14, padx=10, pady=(10, 0), sticky="w")

        self.head_parole_sagge = customtkinter.CTkLabel(self, text="Parole sagge")
        self.head_parole_sagge.grid(row=0, column=15, padx=10, pady=(10, 0), sticky="w")

        self.head_mostra_player_sheet = customtkinter.CTkLabel(self, text="Scheda")
        self.head_mostra_player_sheet.grid(row=0, column=16, padx=10, pady=(10, 0), sticky="w")

        self.head_pesca_carta = customtkinter.CTkLabel(self, text="Pesca")
        self.head_pesca_carta.grid(row=0, column=17, padx=10, pady=(10, 0), sticky="w")

        self.head_pennichella = customtkinter.CTkLabel(self, text="Pennichella")
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
        setattr(self.check_box_values.fastidio, f'{player.id}', customtkinter.IntVar())
        setattr(self.check_box_values.spocchia, f'{player.id}', customtkinter.IntVar())
        setattr(self.check_box_values.scenate_fatte, f'{player.id}', customtkinter.IntVar())
        setattr(self.check_box_values.necrologio, f'{player.id}', customtkinter.IntVar())
        setattr(self.check_box_values.parole_sagge, f'{player.id}', customtkinter.IntVar())
        
        fastidio_cb = getattr(self.check_box_values.fastidio, f'{player.id}')
        spocchia_cb = getattr(self.check_box_values.spocchia, f'{player.id}')
        scenate_fatte_cb = getattr(self.check_box_values.scenate_fatte, f'{player.id}')
        necrologio_cb = getattr(self.check_box_values.necrologio, f'{player.id}')
        parole_sagge_cb = getattr(self.check_box_values.parole_sagge, f'{player.id}')


        self.name = customtkinter.CTkLabel(self, text=player.name)
        self.players_id[player.id] = dict()

        # 4 checkbox Fastidio
        self.name.grid(row=self.player_row, column=0, padx=10, pady=(10, 0), sticky="w")



        self.players_id[player.id]['fastidio_1'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=1  , offvalue=-1)
        self.players_id[player.id]['fastidio_1'].grid(row=self.player_row, column=1, padx=0, pady=0, sticky="w")

        self.players_id[player.id]['fastidio_2'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=2  , offvalue=-2)
        self.players_id[player.id]['fastidio_2'].grid(row=self.player_row, column=2, padx=0, pady=0, sticky="w")

        self.players_id[player.id]['fastidio_3'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=3  , offvalue=-3)
        self.players_id[player.id]['fastidio_3'].grid(row=self.player_row, column=3, padx=0, pady=0, sticky="w")

        self.players_id[player.id]['fastidio_4'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "fastidio"), 
                                                                             variable=fastidio_cb, onvalue=4  , offvalue=-4)
        self.players_id[player.id]['fastidio_4'].grid(row=self.player_row, column=4, padx=0, pady=0, sticky="w")

        # 1 CTkCheckBox Scenata
        self.players_id[player.id]['scenata'] = customtkinter.CTkButton(self, text="Scenata!", width=10, command=lambda: self.master.scenata(player))
        self.players_id[player.id]['scenata'].grid(row=self.player_row, column=5, padx=15, pady=0, sticky="w")

        # 4 CTkCheckBox Spocchia
        self.players_id[player.id]['spocchia_1'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=1  , offvalue=-1)
        self.players_id[player.id]['spocchia_1'].grid(row=self.player_row, column=6, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['spocchia_2'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=2  , offvalue=-2)
        self.players_id[player.id]['spocchia_2'].grid(row=self.player_row, column=7, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['spocchia_3'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=3  , offvalue=-3)
        self.players_id[player.id]['spocchia_3'].grid(row=self.player_row, column=8, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['spocchia_4'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "spocchia"), 
                                                                             variable=spocchia_cb, onvalue=4  , offvalue=-4)
        self.players_id[player.id]['spocchia_4'].grid(row=self.player_row, column=9, padx=0, pady=0, sticky="w")

        # 1 CTkCheckBox Pettegolezzo
        self.players_id[player.id]['pettegolezzo'] = customtkinter.CTkButton(self, text="Pettegolezzo", width=10, command=lambda: self.master.pettegolezzo(player)) 
        self.players_id[player.id]['pettegolezzo'].grid(row=self.player_row, column=10, padx=15, pady=0, sticky="w")

        # 3 CTkCheckBox Scenate fatte
        self.players_id[player.id]['scenate_fatte_1'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "scenate_fatte"), 
                                                                             variable=scenate_fatte_cb, onvalue=1  , offvalue=-1)
        self.players_id[player.id]['scenate_fatte_1'].grid(row=self.player_row, column=11, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['scenate_fatte_2'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "scenate_fatte"), 
                                                                             variable=scenate_fatte_cb, onvalue=2  , offvalue=-2)
        self.players_id[player.id]['scenate_fatte_2'].grid(row=self.player_row, column=12, padx=0, pady=0, sticky="w")
        self.players_id[player.id]['scenate_fatte_3'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "scenate_fatte"), 
                                                                             variable=scenate_fatte_cb, onvalue=3  , offvalue=-3)
        self.players_id[player.id]['scenate_fatte_3'].grid(row=self.player_row, column=13, padx=0, pady=0, sticky="w")

        # 1 CTkCheckBox Necrologio
        self.players_id[player.id]['necrologio'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "necrologio"), 
                                                                             variable=necrologio_cb, onvalue=1  , offvalue=-1)
        self.players_id[player.id]['necrologio'].grid(row=self.player_row, column=14, padx=15, pady=0, sticky="w")

        # 1 CTkCheckBox Parole sagge
        self.players_id[player.id]['parole_sagge'] = customtkinter.CTkCheckBox(self, text="", width=1, 
                                                                             command=lambda: self.master.checkbox_toggle(player, "parole_sagge"), 
                                                                             variable=parole_sagge_cb, onvalue=1  , offvalue=-1)
        self.players_id[player.id]['parole_sagge'].grid(row=self.player_row, column=15, padx=15, pady=0, sticky="w")

        # 1 CTkCheckBox Mostra scheda
        self.players_id[player.id]['mostra_player_sheet'] = customtkinter.CTkButton(self, text="Scheda", width=10 , command=lambda: self.master.show_player_sheet(player))
        self.players_id[player.id]['mostra_player_sheet'].grid(row=self.player_row, column=16, padx=15, pady=0, sticky="w")

        # 1 CTkButton per pescare una carta
        self.players_id[player.id]['pesca_carta'] = customtkinter.CTkButton(self, text="Pesca", width=10, command=lambda: self.master.pesca(player))
        self.players_id[player.id]['pesca_carta'].grid(row=self.player_row, column=17, padx=15, pady=0, sticky="w")

        self.players_id[player.id]['pennichella'] = customtkinter.CTkButton(self, text="Pennichella", width=10, command=lambda: self.master.pennichella(player))
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
            

class card_frame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #crea a frame on the left to show the briscola card
        self.briscola_frame = customtkinter.CTkFrame(self)
        self.briscola_frame.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.show_briscola_card()

        #crea a frame on the right to show the cards of the player
        self.player_frame = customtkinter.CTkFrame(self)
        self.player_frame.grid(row=0, column=1, sticky="w", padx=10, pady=10)
        self.show_player_cards(self.master.mazzo.last_card)

        # crea un fram con le informazioni sulla carta pescata
        self.info_frame = customtkinter.CTkFrame(self)
        self.info_frame.grid(row=0, column=2, sticky="w", padx=10, pady=10)
        self.show_info_card(self.master.mazzo.last_card)
    
    def show_info_card(self, card):
        # remove all widgets from the frame
        for widget in self.info_frame.winfo_children():
            widget.destroy()


        # laber with card name
        i = 0
        card_name = customtkinter.CTkLabel(self.info_frame, text=card.name)
        card_name.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
        i += 1
        if card.seme == self.master.briscola.seme:
            # show a CTkLabel in Dark Green saying the card is of Briscola
            briscola_label = customtkinter.CTkLabel(self.info_frame, text="Briscola", text_color="green" )
            briscola_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1
            successo = customtkinter.CTkLabel(self.info_frame, text="Successo", text_color="green")
            successo.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1
            
            if card.value in [2, 4, 5, 6 ,7]:
                spocchia_label = customtkinter.CTkLabel(self.info_frame, text="Spocchia (2)", )
                self.master.last_card_stats.spocchia = 2
                spocchia_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value in [8, 9, 10]:
                spocchia_label = customtkinter.CTkLabel(self.info_frame, text="Spocchia (2/3)", )
                self.master.last_card_stats.spocchia = 2
                spocchia_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value == 3:
                spocchia_label = customtkinter.CTkLabel(self.info_frame, text="Spocchia (4)", )
                self.master.last_card_stats.spocchia = 4
                spocchia_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                parole_sagge = customtkinter.CTkLabel(self.info_frame, text="Parfole Sagge", )
                self.master.last_card_stats.parole_sagge = True
                parole_sagge.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            else:
                pettegolezzo = customtkinter.CTkLabel(self.info_frame, text="Pettegolezzo", )
                pettegolezzo.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                cambia_briscola = customtkinter.CTkLabel(self.info_frame, text="Cambia Briscola", )
                cambia_briscola.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1

        else:
            # show a CTkLabel in Dark Red saying the card is not of Briscola
            briscola_label = customtkinter.CTkLabel(self.info_frame, text="Non Briscola", text_color="red")
            briscola_label.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1
            
            fallimento = customtkinter.CTkLabel(self.info_frame, text="Fallimento", text_color="Red")
            fallimento.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
            i += 1

            if card.value in [2, 4, 5, 6 ,7]:
                fastidio = customtkinter.CTkLabel(self.info_frame, text="Fastidio (1)", )
                self.master.last_card_stats.fastidio = 1
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                lamentela = customtkinter.CTkLabel(self.info_frame, text="Lamentela", )
                lamentela.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value in [8, 9, 10]:
                fastidio = customtkinter.CTkLabel(self.info_frame, text="Fastidio (2)", )
                self.master.last_card_stats.fastidio = 2
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                lamentela = customtkinter.CTkLabel(self.info_frame, text="Lamentela", )
                lamentela.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            elif card.value == 3:
                fastidio = customtkinter.CTkLabel(self.info_frame, text="Fastidio (3)", )
                self.master.last_card_stats.fastidio = 3
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                sproloquio = customtkinter.CTkLabel(self.info_frame, text="Sproloquio", )
                sproloquio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
            else:
                fastidio = customtkinter.CTkLabel(self.info_frame, text="Fastidio (4)", )
                self.master.last_card_stats.fastidio = 4
                fastidio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1
                necrologio = customtkinter.CTkLabel(self.info_frame, text="Necrologio", )
                self.master.last_card_stats.necrologio = True
                necrologio.grid(row=i, column=0, sticky="nsew", padx=10, pady=10)
                i += 1


    def show_briscola_card(self):    
        my_image = customtkinter.CTkImage(light_image=Image.open(self.master.briscola.path),
                                  dark_image=Image.open(self.master.briscola.path),
                                  size=(177, 285))
        image_label = customtkinter.CTkLabel(self.briscola_frame, image=my_image, text="")
        image_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def show_player_cards(self, card):
        my_image = customtkinter.CTkImage(light_image=Image.open(card.path),
                                  dark_image=Image.open(card.path),
                                  size=(177, 285))
        image_label = customtkinter.CTkLabel(self.player_frame, image=my_image, text="")
        image_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


class Gui(customtkinter.CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.mazzo = Mazzo()
        self.last_card_stats = LastCardStats()
        self.mazzo.pesca()
        self.briscola = self.mazzo.last_card
        self.mazzo.pesca()


        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

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

        self.players = list()
        if "players.json" in listdir():
            json_players = json.loads(open("players.json", "r").read())
            self.players = Player.from_json(json_players)

            for player in self.players:
                self.player_frame.add_player(player)
                self.last_card_stats = LastCardStats()
                self.player_frame.update_playerid_stats(player)
        
        self.card_frame = card_frame(self)
        self.card_frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=10, columnspan=COLUMNS-1)
   
    def create_player(self) -> None:
        player_id = len(self.players) + 1
        # Get Player Nome
        dialog = customtkinter.CTkInputDialog(text="Nome Player:", title="Nome Player")
        nome = dialog.get_input()  # waits for input

        # Get Player Cognome
        dialog = customtkinter.CTkInputDialog(text="Cognome Player:", title="Cognome Player")
        cognome = dialog.get_input()  # waits for input

        # Get Player Soprannome
        dialog = customtkinter.CTkInputDialog(text="Soprannome Player:", title="Soprannome Player")
        soprannome = dialog.get_input()  # waits for input

        # Get Player Ex
        dialog = customtkinter.CTkInputDialog(text="Ex Professione:", title="Ex Professione")
        ex = dialog.get_input()  # waits for input

        # Get Player Pensionato
        dialog = customtkinter.CTkInputDialog(text="Pensionamento:", title="Pensionamento")
        pensionato = dialog.get_input()  # waits for input

        # Get Player Hobby
        dialog = customtkinter.CTkInputDialog(text="Hobby:", title="Hobby")
        hobby = dialog.get_input()  # waits for input

        # Get Player Circolo
        dialog = customtkinter.CTkInputDialog(text="Circolo:", title="Circolo")
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

    def pesca(self, player=None):
        self.mazzo.pesca()
        self.last_card_stats = LastCardStats()
        self.card_frame.show_player_cards(self.mazzo.last_card)
        self.card_frame.show_info_card(self.mazzo.last_card)
        
        if player is not None:
            self.player_frame.update_playerid_stats(player)
    
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
            pettegolezzo = customtkinter.CTkInputDialog(text="Hai dirtto a creare un nuovo pettegolezzo:", title="Pettegolezzo")
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
        if stat == "fastidio":
            print(player.id, stat, getattr(self.player_frame.check_box_values.fastidio, f'{player.id}').get())
            value = getattr(self.player_frame.check_box_values.fastidio, f'{player.id}').get()
        elif stat == "spocchia":
            print(player.id, stat, getattr(self.player_frame.check_box_values.spocchia, f'{player.id}').get())
            value = getattr(self.player_frame.check_box_values.spocchia, f'{player.id}').get()
        elif stat == "scenate_fatte":
            print(player.id, stat, getattr(self.player_frame.check_box_values.scenate_fatte , f'{player.id}').get())
            value = getattr(self.player_frame.check_box_values.scenate_fatte , f'{player.id}').get()
        elif stat == "necrologio":
            print(player.id, stat, getattr(self.player_frame.check_box_values.necrologio, f'{player.id}').get())
            value = getattr(self.player_frame.check_box_values.necrologio, f'{player.id}').get()
        elif stat == "parole_sagge":
            print(player.id, stat, getattr(self.player_frame.check_box_values.parole_sagge, f'{player.id}').get())
            value = getattr(self.player_frame.check_box_values.parole_sagge, f'{player.id}').get()
        


    def salva_players(self):
        json_players = [player.__dict__ for player in self.players]
        open('players.json', 'w').write(json.dumps(json_players, indent=2))
        self.show_dialog("Salvataggio avvenuto con successo!", "Salvato!")

    def show_dialog(self, title, text):
        if self.custom_dialog_window is None or not self.custom_dialog_window.winfo_exists():
            self.custom_dialog_window = Custom_Dialog(title, text, self) 
        else:
            self.custom_dialog_window.focus()  # if window exists focus it

class Custom_Dialog(customtkinter.CTkToplevel):
    def __init__(self, title, text, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        altezza = 100
        larghezza = len(text) * 7
        print(len(text), larghezza)

        self.geometry(f"{larghezza}x{altezza}")
        self.title(title)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(self, text=text)
        self.label.pack(padx=20, pady=20)


class PlayerSheet(customtkinter.CTkToplevel):
    def __init__(self, player, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
        self.geometry("00x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        COLUMNS = 2
        self.title(f"Scheda di {player.name} {player.cognome}")

        self.head = customtkinter.CTkLabel(self, text=f"EX {player.ex}, {player.pensionato} in pensione, con l'hobby del {player.hobby}", fg_color="gray30", corner_radius=6)
        self.head.grid(row=0, column=0, pady=5, padx=5, sticky="ew", columnspan=COLUMNS)

        # a frame all to the right that will containe nome, cognome, soprannome, circolo
        self.player_info_frame = customtkinter.CTkFrame(self)
        self.player_info_frame.grid(row=1, column=COLUMNS, sticky="n")

        self.name = customtkinter.CTkLabel(self.player_info_frame, text=f"Nome: {player.name}", fg_color="gray30", corner_radius=6)
        self.name.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        self.cognome = customtkinter.CTkLabel(self.player_info_frame, text=f"Cognome: {player.cognome}", fg_color="gray30", corner_radius=6)
        self.cognome.grid(row=1, column=0, pady=5, padx=5, sticky="ew")
        self.soprannome = customtkinter.CTkLabel(self.player_info_frame, text=f"Soprannome: {player.soprannome}", fg_color="gray30", corner_radius=6)
        self.soprannome.grid(row=2, column=0, pady=5, padx=5, sticky="ew")
        self.circolo = customtkinter.CTkLabel(self.player_info_frame, text=f"Circolo: {player.circolo}", fg_color="gray30", corner_radius=6)
        self.circolo.grid(row=3, column=0, pady=5, padx=5, sticky="ew")

        # a frame in position row 1 column 0 that will containe the player status
        self.player_status_frame = customtkinter.CTkFrame(self)
        self.player_status_frame.grid(row=1, column=0, sticky="n")
        # fastidio level
        self.fastidio = customtkinter.CTkLabel(self.player_status_frame, text=f"Fastidio: {player.fastidio}", fg_color="gray30", corner_radius=6)
        self.fastidio.grid(row=0, column=0, pady=5, padx=5, sticky="ew")
        # spocchia level
        self.spocchia = customtkinter.CTkLabel(self.player_status_frame, text=f"Spocchia: {player.spocchia}", fg_color="gray30", corner_radius=6)
        self.spocchia.grid(row=1, column=0, pady=5, padx=5, sticky="ew")

if __name__ == "__main__":
    app = Gui()
    app.mainloop()



    