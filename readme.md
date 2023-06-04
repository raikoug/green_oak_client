# Green Oak
Green Oak è un gioco di ruolo che si può acquistare qua  
https://www.msedizioni.it/prodotto/green-oaks/



# A cosa serve
Vuoi giocare a Green Oak ma siete su Discord?  
L'applicazione Badante non è un granché, quindi ho fatto un client per rendere più facile giocarci.

# Cosa Serve?
Per ora python con un paio di lib, scoprirai quali facendo partire il gioco  
Ricordati di cancellare il mio players.json (di test).

# GetStarted
Clona e dalla root fai partire la gui
```python
python ./Libs/guy.py
```

## Cambiare le carte
Se le carte non ti piacciono, puoi sostituirle dalla cartella, se mantiene la nomenclatura non avrai problemi. 
Nel caso invece tu voglia usare semi diversi dovrai creare (con le stesse chiavi!) un `carte.json` diverso.  
L'applicazione usa `seme` e `value` per decidere cosa scuccede, puoi avere quanti semi vuoi, ma i valori saranno sempre: 
- Asso (1)
- Tre (3)
- Numeri (4,5,6,7)
- Figure (8,9,10)
Altri valori non saranno considerati

# TODO
- [ ] Anzitutto vorrei mettere quelle dannate carte più vicine fra loro
- [ ] Una scheda decisamente migliore
- [x] Usare un dialog senza input quando l'input non serve..
  - [x] Mostrare il titolo della TopLevel
- [ ] Pennichella
- [ ] Leggero refactoring del codice?
- [ ] Far partire lo script dal main magari...


