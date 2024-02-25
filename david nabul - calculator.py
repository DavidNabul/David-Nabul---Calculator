import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Fancy Calculator")
        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=4,
                              width=16, justify='right', background='#F0F0F0')
        self.entry.grid(row=0, column=0, columnspan=4, pady=10)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(master, text=text, padx=20, pady=20, font=('Arial', 16), bg='#4CAF50', fg='white',
                               command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

        # Configure grid weights to make it expandable
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def button_click(self, value):
        if value == 'C':
            self.result_var.set('')
        elif value == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid input")
                self.result_var.set('')
        else:
            current_text = self.result_var.get()
            current_text += value
            self.result_var.set(current_text)


def main():
    root = tk.Tk()
    root.geometry("400x500")
    root.configure(bg='#ECECEC')
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
