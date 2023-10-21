import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self, notes_directory):
        self.notes_directory = notes_directory

    def create_note(self, note):
        filename = f"{note.title}.txt"
        filepath = os.path.join(self.notes_directory, filename)
        with open(filepath, "w") as file:
            file.write(note.content)

    def read_notes(self):
        notes = []
        for filename in os.listdir(self.notes_directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.notes_directory, filename)
                with open(filepath, "r") as file:
                    content = file.read()
                    note = Note(filename[:-4], content)
                    notes.append(note)
        return notes

    def edit_note(self, note_title, new_content):
        filename = f"{note_title}.txt"
        filepath = os.path.join(self.notes_directory, filename)
        with open(filepath, "w") as file:
            file.write(new_content)

    def delete_note(self, note_title):
        filename = f"{note_title}.txt"
        filepath = os.path.join(self.notes_directory, filename)
        os.remove(filepath)

# Пример использования
notes_manager = NoteManager("H:\Testing\Project\PromAtest1")
note1 = Note("Заметка 1", "Содержание заметки 1")
note2 = Note("Заметка 2", "Содержание заметки 2")

notes_manager.create_note(note1)
notes_manager.create_note(note2)

notes = notes_manager.read_notes()
for note in notes:
    print(note.title, note.content)

notes_manager.edit_note("Заметка 1", "Новое содержание заметки 1")

notes = notes_manager.read_notes()
for note in notes:
    print(note.title, note.content)

notes_manager.delete_note("Заметка 2")

notes = notes_manager.read_notes()
for note in notes:
    print(note.title, note.content)