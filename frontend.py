import tkinter as tk
from tkinter import messagebox
from functools import partial
from backend import print_board, check_winner, is_draw  # Import backend functions

def update_board(row, col):
    global board, current_player, buttons

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(board, current_player):
            print_board(board)
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif is_draw(board):
            print_board(board)
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showerror("Invalid Move", "This spot is already taken. Try again.")


# Backend code
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def update_board(row, col):
    global board, current_player, buttons

    if board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner(board, current_player):
            print_board(board)
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif is_draw(board):
            print_board(board)
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showerror("Invalid Move", "This spot is already taken. Try again.")

def reset_board():
    global board, buttons, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")

# Frontend code
root = tk.Tk()
root.title("Tic Tac Toe")

board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text=" ", width=10, height=4,
                           command=partial(update_board, i, j))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

reset_button = tk.Button(root, text="Reset", command=reset_board)
reset_button.grid(row=3, columnspan=3)

root.mainloop()
