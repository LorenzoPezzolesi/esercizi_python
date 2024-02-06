#Realizzare un programma che implementi il gioco della tombola o del bingo. 
#Al fine di far ciò, lo studente implementi le seguenti funzioni:
#1) def genera_cartella(id: int<str>)->dict:
#La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
#N.B.
#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90
#
#
#2) def estrai_numero(numeri_estratti: list[])->int:
#La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.
#
#3) def controlla_cartella(cartella: dict, numeri_estratti[])->list[bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella. Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno(naturalmente per fare terno bisogna aver fatto anche ambo....)
#
#Realizzare un programma che implementi la logica di funzionamento:
#a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
#b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.

import random

def genera_cartella(id: int)->dict:
    riga_1 = 
    riga_2 = 
    riga_3 = 













def estrai_numero(numeri_estratti: list[])->int:
