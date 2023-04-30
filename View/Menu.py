from Presenter.Command import *
from NotesManager import NotesManager

class Menu:
    def __init__(self, notes_manager):
        self.commands = {
            "1": AddNoteCommand(notes_manager),
            "2": DeleteNoteCommand(notes_manager),
            "3": EditNoteCommand(notes_manager),
            "4": ViewNotesCommand(notes_manager),
            "5": SaveNotesCommand(notes_manager),
            "6": ReadNotesCommand(notes_manager),
            "7": SelectionByIndexCommand(notes_manager),
            "8": SelectionByDateCommand(notes_manager),
            "9": ExitCommand()
        }

    def display(self):
        print("1. Add note")
        print("2. Delete note")
        print("3. Edit note")
        print("4. View all notes")
        print("5. Save notes to CSV file")
        print("6. Read notes from CSV file")
        print("7. Search notes by index")
        print("8. Search notes by date")
        print("9. Exit")

    def run(self):
        while True:
            self.display()
            choice = input("Enter choice: ")
            command = self.commands.get(choice)
            if command:
                command.execute()
            else:
                print("Invalid choice")

if __name__ == "__main__":
    notes_manager = NotesManager()
    menu = Menu(notes_manager)
    menu.run()