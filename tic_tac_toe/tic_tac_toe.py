import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window, text=" ", font=("Helvetica", 25), width=10, height=5,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                self.show_winner()
            elif self.check_draw():
                self.show_draw()
            else:
                self.switch_player()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def show_winner(self):
        winner = f"Player {self.current_player} wins!"
        messagebox.showinfo("Congratulations", winner)
        self.reset_board()

    def show_draw(self):
        messagebox.showinfo("Draw", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
