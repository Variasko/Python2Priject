import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class NoteEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Редактор заметок")

        self.notes = []
        self.load_notes()

        self.create_widgets()

    def create_widgets(self):
        self.note_listbox = tk.Listbox(self.root, width=50, height=20)
        self.note_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.note_listbox.bind('<<ListboxSelect>>', self.on_select)

        self.note_text = tk.Text(self.root, width=50, height=20)
        self.note_text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(self.root, text="Добавить заметку", command=self.add_note)
        self.add_button.pack(side=tk.TOP)

        self.edit_button = tk.Button(self.root, text="Изменить заметку", command=self.edit_note)
        self.edit_button.pack(side=tk.TOP)

        self.delete_button = tk.Button(self.root, text="Удалить заметку", command=self.delete_note)
        self.delete_button.pack(side=tk.TOP)

        self.complete_button = tk.Button(self.root, text="Пометить как выполненную", command=self.mark_complete)
        self.complete_button.pack(side=tk.TOP)

        self.update_listbox()

    def load_notes(self):
        try:
            if os.path.exists('notes.json'):
                with open('notes.json', 'r') as file:
                    self.notes = json.load(file)
        except:
            pass
    def save_notes(self):
        with open('notes.json', 'w') as file:
            json.dump(self.notes, file, indent=4)

    def update_listbox(self):
        self.note_listbox.delete(0, tk.END)
        for note in self.notes:
            status = " [Выполнено]" if note.get("completed", False) else ""
            self.note_listbox.insert(tk.END, f"{note['title']}{status}")

    def on_select(self, event):
        selected_index = self.note_listbox.curselection()
        if selected_index:
            note = self.notes[selected_index[0]]
            self.note_text.delete(1.0, tk.END)
            self.note_text.insert(tk.END, note['content'])

    def add_note(self):
        title = simpledialog.askstring("Добавить заметку", "Введите заголовок заметки:")
        if title:
            content = self.note_text.get(1.0, tk.END).strip()
            self.notes.append({"title": title, "content": content, "completed": False})
            self.save_notes()
            self.update_listbox()

    def edit_note(self):
        selected_index = self.note_listbox.curselection()
        if selected_index:
            note = self.notes[selected_index[0]]
            new_title = simpledialog.askstring("Изменить заметку", "Введите новый заголовок заметки:", initialvalue=note['title'])
            if new_title:
                note['title'] = new_title
                note['content'] = self.note_text.get(1.0, tk.END).strip()
                self.save_notes()
                self.update_listbox()

    def delete_note(self):
        selected_index = self.note_listbox.curselection()
        if selected_index:
            del self.notes[selected_index[0]]
            self.save_notes()
            self.update_listbox()

    def mark_complete(self):
        selected_index = self.note_listbox.curselection()
        if selected_index:
            note = self.notes[selected_index[0]]
            note['completed'] = not note.get('completed', False)
            self.save_notes()
            self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteEditor(root)
    root.mainloop()
