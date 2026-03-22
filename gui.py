import tkinter as tk
from tkinter import messagebox
from smart_editor import SmartEditor

class SmartEditorUI:
    def __init__(self, root):
        self.editor = SmartEditor()
        self.root = root
        self.root.title("Smart Editor Pro")

        # Área de texto
        self.display = tk.Text(root, height=10, width=60, bg="#1e1e1e", fg="white")
        self.display.pack(pady=10)

        # Input
        self.input = tk.Entry(root, width=40)
        self.input.pack()

        # Botones
        frame = tk.Frame(root)
        frame.pack(pady=5)

        tk.Button(frame, text="Escribir", command=self.write).grid(row=0, column=0)
        tk.Button(frame, text="Borrar", command=self.delete).grid(row=0, column=1)
        tk.Button(frame, text="Deshacer", command=self.undo).grid(row=0, column=2)
        tk.Button(frame, text="Rehacer", command=self.redo).grid(row=0, column=3)

        # Info
        self.info = tk.Label(root, text="Caracteres: 0")
        self.info.pack()

        tk.Button(root, text="Ver historial", command=self.show_log).pack()

    def refresh(self):
        self.display.delete(1.0, tk.END)
        self.display.insert(tk.END, self.editor.get_text())
        self.info.config(text=f"Caracteres: {self.editor.length()}")

    def write(self):
        try:
            text = self.input.get()
            self.editor.write(text)
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete(self):
        try:
            n = int(self.input.get())
            self.editor.delete(n)
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def undo(self):
        try:
            self.editor.undo()
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def redo(self):
        try:
            self.editor.redo()
            self.refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_log(self):
        history = "\n".join(self.editor.get_log())
        messagebox.showinfo("Historial", history)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartEditorUI(root)
    root.mainloop()