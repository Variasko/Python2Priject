import tkinter as tk
from tkinter import messagebox as mb

# функция проверки победителя
def check_winner():

    global board

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# функция проверки доски на заполненность
def is_board_fill():

    global board

    for row in board:
        if "" in row:
            return False
    return True

def reset_game():

    global board, buttons, current_player

    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

        # функция обработки нажатия на кнопку
def on_button_click(row, column):

    global board, buttons, current_player

    if board[row][column] == "" and not check_winner():
        board[row][column] = current_player
        # тут config будет подчёркиваться так как, buttons это список, и
        # ide(pycharm) не знает, а точно ли там кнопки из tkinter, поэтому
        # и намекает, мол проверь, а то может вылезти ошибка
        buttons[row][column].config(text=current_player)

    if check_winner():
        mb.showinfo("Победитель", f"Победил игрок: {current_player}")
        reset_game()

    elif is_board_fill():
        mb.showinfo("Ничья!", "Ничья!")
        reset_game()
    else:
        if current_player == 'X':
            current_player = "O"
        else:
            current_player = 'X'

root = tk.Tk()

root.title = "Крестики-нолики"

current_player = 'X'

board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 20),
                                       width=5, height=2,
                                       command=lambda row=i, col=j: on_button_click(row, col))

        # тут grid будет подчёркиваться так как, buttons это список, и
        # ide(pycharm) не знает, а точно ли там кнопки из tkinter, поэтому
        # и намекает, мол проверь, а то может вылезти ошибка
        buttons[i][j].grid(row=i, column=j)

root.mainloop()