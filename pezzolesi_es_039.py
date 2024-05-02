#from flask import Flask, render_template
import json

def get_flashcard_by_id(id: int) -> None:
    with open("pezzolesi_es_039.json","r") as f:
        flashcards=json.load(f)
        for flashcard in flashcards:
            if flashcard["id"]==id:
                return flashcard

def prompt_for_id() -> int:
    id = int(input("Scegli un id da 1 a 3:"))
    flashcard = get_flashcard_by_id(id)
    print(flashcard["question"])

if __name__=="__main__":
    prompt_for_id()

def prompt_for_answer() -> str:
    id = int(input("Scegli un id da 1 a 3:"))





