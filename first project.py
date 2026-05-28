import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Python Calculator")
        self.root.geometry("420x600")
        self.root.resizable(False, False)

        self.dark_mode = True

        self.expression = ""
        self.history = []

        self.input_text = tk.StringVar()

        self.create_ui()
        self.apply_theme()

    def create_ui(self):

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(fill="both")

        self.input_field = tk.Entry(
            self.input_frame,
            textvariable=self.input_text,
            font=('Arial', 24),
            bd=8,
            relief=tk.RIDGE,
            justify='right'
        )
        self.input_field.pack(ipady=20, fill='both', padx=10, pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        buttons = [
            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'pow'],
            ['1', '2', '3', '-', 'log'],
            ['0', '.', '%', '+', 'sin'],
            ['C', 'DEL', '=', 'History', 'Theme']
        ]

        for row in buttons:
            row_frame = tk.Frame(self.button_frame)
            row_frame.pack(expand=True, fill='both')

            for btn in row:
                button = tk.Button(
                    row_frame,
                    text=btn,
                    font=('Arial', 16),
                    height=2,
                    width=5,
                    command=lambda x=btn: self.on_button_click(x)
                )
                button.pack(side='left', expand=True, fill='both', padx=2, pady=2)

        self.root.bind("<Key>", self.key_input)

    def apply_theme(self):

        bg = "#1e1e1e" if self.dark_mode else "#f4f4f4"
        fg = "white" if self.dark_mode else "black"
        btn_bg = "#333333" if self.dark_mode else "#dddddd"

        self.root.configure(bg=bg)
        self.input_frame.configure(bg=bg)
        self.button_frame.configure(bg=bg)

        self.input_field.configure(
            bg=btn_bg,
            fg=fg,
            insertbackground=fg
        )

        for widget in self.button_frame.winfo_children():
            for btn in widget.winfo_children():
                btn.configure(
                    bg=btn_bg,
                    fg=fg,
                    activebackground="#555555",
                    activeforeground="white"
                )

    def on_button_click(self, char):

        try:
            if char == "=":
                result = str(eval(self.expression))
                self.history.append(f"{self.expression} = {result}")
                self.expression = result
                self.input_text.set(result)

            elif char == "C":
                self.expression = ""
                self.input_text.set("")

            elif char == "DEL":
                self.expression = self.expression[:-1]
                self.input_text.set(self.expression)

            elif char == "sqrt":
                result = str(math.sqrt(eval(self.expression)))
                self.history.append(f"√({self.expression}) = {result}")
                self.expression = result
                self.input_text.set(result)

            elif char == "pow":
                self.expression += "**"
                self.input_text.set(self.expression)

            elif char == "log":
                result = str(math.log10(eval(self.expression)))
                self.history.append(f"log({self.expression}) = {result}")
                self.expression = result
                self.input_text.set(result)

            elif char == "sin":
                result = str(math.sin(math.radians(eval(self.expression))))
                self.history.append(f"sin({self.expression}) = {result}")
                self.expression = result
                self.input_text.set(result)

            elif char == "History":
                self.show_history()

            elif char == "Theme":
                self.dark_mode = not self.dark_mode
                self.apply_theme()

            else:
                self.expression += str(char)
                self.input_text.set(self.expression)

        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
            self.input_text.set("")

    def show_history(self):

        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("350x400")

        text = tk.Text(history_window, font=('Arial', 14))
        text.pack(fill='both', expand=True)

        for item in self.history:
            text.insert(tk.END, item + "\n")

    def key_input(self, event):

        key = event.char

        allowed = "0123456789+-*/.%"

        if key in allowed:
            self.expression += key
            self.input_text.set(self.expression)

        elif event.keysym == "Return":
            self.on_button_click("=")

        elif event.keysym == "BackSpace":
            self.on_button_click("DEL")


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()