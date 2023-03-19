import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Untitled - Notepad")

        # create the text area
        self.textarea = tk.Text(master, undo=True)
        self.textarea.pack(fill='both', expand=True)

        # create the menu
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new_file)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        master.config(menu=menubar)

        # track changes to the text area
        self.textarea.bind('<Key>', self.on_change)

        # track the current file
        self.current_file = None

    def new_file(self):
        self.textarea.delete('1.0', 'end')
        self.current_file = None
        self.master.title("Untitled - Notepad")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text = file.read()
                self.textarea.delete('1.0', 'end')
                self.textarea.insert('1.0', text)
                self.current_file = file_path
                self.master.title(self.current_file + " - Notepad")

    def save_file(self):
        if not self.current_file:
            self.current_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if not self.current_file:
                return
            self.master.title(self.current_file + " - Notepad")
        text = self.textarea.get('1.0', 'end')
        with open(self.current_file, 'w') as file:
            file.write(text)

    def on_change(self, event):
        self.master.title("*" + self.master.title())

if __name__ == '__main__':
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
