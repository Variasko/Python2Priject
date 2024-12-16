from tkinter import *

calculators = [
    [1, 2, 3, "+"],
    [4, 5, 6, "-"],
    [7, 8, 9, "*"],
    [".", 0, "", "/"]
]

class Calculator(Tk):
    def __init__(self, title: str, size: tuple):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        self.outputEntry = Entry(self, width=20, font=("Arial", 20), justify=RIGHT)
        self.outputEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        for i in range(4):
            for j in range(4):
                button_text = calculators[i][j]
                if button_text == "":
                    continue
                button = Button(self, text=button_text, height=2, width=5, font=("Arial", 18),
                                command=lambda text=button_text: self.button_click(text))
                button.grid(row=i+1, column=j, padx=5, pady=5)

        buttonEqual = Button(self, text="=", width=22, height=2, font=("Arial", 18),
                             command=self.calculate_result)
        buttonEqual.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

    def button_click(self, text: str):
        current_text = self.outputEntry.get()
        if text == "=":
            self.calculate_result()
        else:
            self.outputEntry.delete(0, END)
            self.outputEntry.insert(END, current_text + str(text))

    def calculate_result(self):
        try:
            example = self.outputEntry.get()
            result = eval(example)
            self.outputEntry.delete(0, END)
            self.outputEntry.insert(END, result)
        except Exception as e:
            self.outputEntry.delete(0, END)
            self.outputEntry.insert(END, "Error")

if __name__ == '__main__':
    root = Calculator("Калькулятор", (360, 475))
    root.mainloop()
