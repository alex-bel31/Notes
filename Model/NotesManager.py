from Note import Note
import csv

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def delete_note_by_index(self, index):
        self.notes.pop(index)

    def edit_note_by_index(self, index, new_title, new_body):
        self.notes[index].title = new_title
        self.notes[index].body = new_body

    def view_all_notes(self):
        for i, note in enumerate(self.notes):
            print(f"{i+1}. {note.title}\n{note.body}\n")

    def save_notes_to_csv(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "date","title", "body"])
            for note in self.notes:
                writer.writerow([note.id, note.date, note.title, note.body])

    def load_notes_from_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                note = Note(row[0], row[1])
                self.add_note(note) 

    def get_notes_by_date(self, date):
        return [note for note in self.notes if note.date == date] 
    
    def view_note_by_index(self, index):
        note = self.notes[index]
        print(f"{note.title}\n{note.body}\n")
