import json
import os
from datetime import datetime

def create_note():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    note_id = len(notes) + 1
    note_title = input("Введите заголовок заметки:")
    note_body = input("Введите текст заметки:")

    note= {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes()

    print("Змаетка успешно создана")

def read_notes():
        for note in notes:
            print(f"ID: {note['id']}nЗаголовок: {note['title']}nТекст: {note['body']}nДата/Время: {note['timestamp']}n")


def edit_note():
        note_id = int(input("Введите ID заметки, которую необходимо отредактировать:"))
        note_index = -1

        for index, note in enumerate(notes):
            if note['id'] == note_id:
                note_index = index
                break
        
        if note_index != -1:
            note_title = input("Введите новый заголовок заметки")
            note_body= input("Введите новый текст зметки")

            notes[note_index]['title']=note_title
            notes[note_index]['body']=note_body
            notes[note_index]['timestamp']=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            save_notes()
            print("Заметка успешно отредактирована")
        else:
            print("Змаетка с указанным ID не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки, которую необходимо удалить:"))
    note_index = -1

    for index, note in enumerate(notes):
            if note['id'] == note_id:
                note_index = index
                break
        
            if note_index != -1:
                del notes[note_index]
                save_notes()
                print("Замтека успешно удалена")
            else:
                print("Змаетка с указанным ID не найдена")

def save_notes():
      with open("notes.json", "w") as file:
            json.dump(notes, file)


def load_notes():
      if os.path.exists("notes.json"):
            with open("notes.json", "r") as file:
                  notes.extend(json.load(file))

notes = []

load_notes()

while True:
      print("nМеню")
      print("1. Создать заметку")
      print("2. Просмотреть все заметки")
      print("3. Редактировать заметку")
      print("4. Удалить заметку")
      print("5. Выход")
      choice = input("Выберите действие")
      if choice == "1":
        create_note()
        if choice == "2":
            read_notes()
        if choice == "3":
            edit_note()
        if choice == "4":
            delete_note()
        if choice == "5":
            break
        else:
            print("Некорректный выбор. Попробуйте снова")
      
