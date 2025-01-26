import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Check  rows/columns for winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    # look if cells are all full
    return all(cell != " " for row in board for cell in row)

def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] == " ":
        # Update the button text + the board state
        buttons[row][col]["text"] = players[current_player]
        board[row][col] = players[current_player]

        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            reset_board()
            return

        if is_full(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return

        # Switch player
        current_player = 1 - current_player
    else:
        messagebox.showwarning("Invalid Move", "That spot is already taken. Try again.")

def reset_board():
    global board, current_player

    # Clear the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = " "
    current_player = 0

def create_gui():
    global buttons

    # Main window
    root = tk.Tk()
    root.title("Tic Tac Toe")

    # Create the buttons
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text=" ", font=("Arial", 24), width=5, height=2,
                               command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col)
            buttons[row][col] = button

    # Add a reset button
    reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=reset_board)
    reset_button.grid(row=3, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    players = ["X", "O"]
    current_player = 0
    board = [[" " for _ in range(3)] for _ in range(3)]
    buttons = [[None for _ in range(3)] for _ in range(3)]

    create_gui()
