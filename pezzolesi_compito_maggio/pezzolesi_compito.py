import json

#2)
def read_file_json(filename: str) -> list:
    with open(filename,"r") as f:
        colors_list= json.load(f)
        return colors_list

#3)
def update_file_json(filename: str, colors_list: list) -> None:
    with open(filename,"w") as f:
        json.dump(colors_list, f)

#4)
def add_new_user_data(name: str, surname:str, favourite_color: str,colors_list: list) -> None:
    user_item = {   "name" : name,
                    "surname" : surname,
                    "favourite_color" : favourite_color
                }
    
    colors_list.append(user_item)

#5)
def get_favourites_colors(filename: str) -> list:
    read_file_json(filename)
    return


#6)
#def get_colors_by_name(filename: str, name: str, surname: str) -> list:



#Parte 1)
def CLI_application():
    #Leggo il contenuto del file in una lista
    filename = "colors.json"
    colors_list = read_file_json(filename)
    print(colors_list)

    #Aggiungo un dizionario alla lista di dizionari e non al file
    name = input("Dimmi quale è il tuo nome")
    surname = input("Dimmi quale è il tuo cognome")
    favourite_color = input("Dimmi quale è il tuo colore preferito")
    add_new_user_data(name, surname, favourite_color, colors_list) 

    #Aggiorno il json con i nuovi dati
    update_file_json(filename, colors_list)


CLI_application()

#Parte 2)
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "pagina iniziale"


@app.route("/color_report/<string: color>")
def color_report(string):
    pass
