from Note import Note

class AddNoteCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager

    def execute(self):
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        note = Note(title, body)
        self.notes_manager.add_note(note)

class DeleteNoteCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager

    def execute(self):
        index = int(input("Enter note index to delete: ")) - 1
        self.notes_manager.delete_note_by_index(index)

class EditNoteCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager

    def execute(self):
        index = int(input("Enter note index to edit: ")) - 1
        new_title = input("Enter new title: ")
        new_body = input("Enter new body: ")
        self.notes_manager.edit_note_by_index(index, new_title, new_body)

class ViewNotesCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager

    def execute(self):
        self.notes_manager.view_all_notes()

class SaveNotesCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager

    def execute(self):
        filename = input("Enter filename to save notes to: ")
        format = ".csv"
        result = "".join([filename, format])
        self.notes_manager.save_notes_to_csv(result)

class ReadNotesCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager

    def execute(self):
        filename = input("Enter filename to read notes to: ")
        self.notes_manager.load_notes_from_csv(filename)


class SelectionByIndexCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager    

    def execute(self):
        index = int(input("Enter index: ")) - 1
        self.notes_manager.view_note_by_index(index)

class SelectionByDateCommand:
    def __init__(self, notes_manager):
        self.notes_manager = notes_manager 

    def execute(self):
        date = input("Enter date: ")
        self.notes_manager.get_notes_by_date(date)

class ExitCommand:
    def execute(self):
        exit()