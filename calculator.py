import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x400")

        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()

        self.result_display = tk.Entry(self, textvariable=self.result_var, justify='right', font=("Helvetica", 20))
        self.result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=25)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self, text=text, font=("Helvetica", 16), width=5, height=2, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, button_text):
        if button_text == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'C':
            self.result_var.set("")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button_text)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
