from tkinter import *
from tkinter.messagebox import *


class SignInWindow:
    def __init__(self, root: Tk):
        self.root = root
        self.root.title("Авторизация")
        self.root.configure(bg="#e0e0e0")

        self.create_widgets()

    def create_widgets(self):
        self.sign_in_label = Label(
            self.root,
            text="Авторизация",
            font=("Helvetica", 25, "bold"),
            bg="#e0e0e0"
        )
        self.login_label = Label(
            self.root,
            text="Логин:",
            font=("Helvetica", 20),
            bg="#e0e0e0"
        )
        self.password_label = Label(
            self.root,
            text="Пароль:",
            font=("Helvetica", 20),
            bg="#e0e0e0"
        )
        self.login_entry = Entry(
            self.root,
            font=("Helvetica", 20),
            bd=2,
            relief="solid"
        )
        self.password_entry = Entry(
            self.root,
            font=("Helvetica", 20),
            bd=2,
            relief="solid",
            show="*"
        )
        self.sign_in_button = Button(
            self.root,
            text="Войти",
            command=self.check_sign_in,
            font=("Helvetica", 20, "bold"),
            bg="#007BFF",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            highlightthickness=0
        )
        self.sign_in_button.config(highlightbackground="#007BFF",
                                   highlightcolor="#007BFF")

        self.register_button = Button(
            self.root,
            text="Регистрация",
            command=self.show_under_development,
            font=("Helvetica", 20, "bold"),
            bg="#28a745",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            highlightthickness=0
        )
        self.register_button.config(highlightbackground="#28a745",
                                    highlightcolor="#28a745")

        self.forgot_password_button = Button(
            self.root,
            text="Забыли пароль?",
            command=self.show_under_development,
            font=("Helvetica", 20, "bold"),
            bg="#dc3545",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            highlightthickness=0
        )
        self.forgot_password_button.config(highlightbackground="#dc3545",
                                           highlightcolor="#dc3545")

        self.sign_in_label.grid(row=0, column=0, columnspan=2,
                                pady=20, padx=20)

        self.login_label.grid(row=1, column=0, columnspan=1,
                              pady=10, padx=20, sticky=E)

        self.password_label.grid(row=2, column=0, columnspan=1,
                                 pady=10, padx=20, sticky=E)

        self.login_entry.grid(row=1, column=1, columnspan=1,
                              pady=10, padx=20, sticky=W)

        self.password_entry.grid(row=2, column=1, columnspan=1,
                                 pady=10, padx=20, sticky=W)

        self.sign_in_button.grid(row=3, column=0, columnspan=1,
                                 pady=20, padx=(20, 10))

        self.register_button.grid(row=3, column=1, columnspan=1,
                                  pady=20, padx=(10, 20))

        self.forgot_password_button.grid(row=4, column=0,
                                         columnspan=2, pady=20)

    def check_sign_in(self):
        people = {
            "parent1": ["parent1", "Родитель"],
            "parent2": ["parent2", "Родитель"],
            "parent3": ["parent3", "Родитель"],
            "student1": ["student1", "Студент"],
            "student2": ["student2", "Студент"],
            "student3": ["student3", "Студент"],
            "teacher1": ["teacher1", "Учитель"],
            "teacher2": ["teacher2", "Учитель"],
            "teacher3": ["teacher3", "Учитель"]
        }

        login = self.login_entry.get()
        password = self.password_entry.get()
        
        if login == "" and password == "":
            showerror("Ошибка!",
                      "Заполните поле логин или пароль!")
            return

        try:
            if people[login][0] == password:
                showinfo("Успех!",
                         f"Добро пожаловать, {people[login][1]}")
        except KeyError:
            showerror("Ошибка!",
                      "Неверный логин или пароль!")

    def show_under_development(self):
        showinfo("Информация",
                 "Функция в разработке")


if __name__ == '__main__':
    root = Tk()
    app = SignInWindow(root)
    root.mainloop()
