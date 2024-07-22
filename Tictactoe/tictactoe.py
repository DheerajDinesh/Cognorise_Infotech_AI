import tkinter as tk
from tkinter import messagebox
import random

# Initialize the board
board = [' ' for _ in range(9)]

def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    return ' ' not in board

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    elif check_winner(board, 'X'):
        return -1
    elif check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def easy_ai_move(board):
    available_moves = [i for i in range(9) if board[i] == ' ']
    move = random.choice(available_moves)
    board[move] = 'O'
    return move

def medium_ai_move(board):
    if random.random() < 0.5:
        return easy_ai_move(board)
    else:
        return minimax_ai_move(board)

def minimax_ai_move(board):
    best_score = -float('inf')
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'
    return best_move

def ai_move(board, difficulty):
    if difficulty == 'Easy':
        return easy_ai_move(board)
    elif difficulty == 'Medium':
        return medium_ai_move(board)
    else:
        return minimax_ai_move(board)

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title('Tic Tac Toe')
        self.buttons = []
        self.difficulty = tk.StringVar(value='Hard')
        self.create_widgets()
        self.create_buttons()

    def create_widgets(self):
        # Difficulty selector
        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.pack()

        difficulty_label = tk.Label(difficulty_frame, text="Select Difficulty: ")
        difficulty_label.pack(side=tk.LEFT)

        difficulty_menu = tk.OptionMenu(difficulty_frame, self.difficulty, 'Easy', 'Medium', 'Hard')
        difficulty_menu.pack(side=tk.LEFT)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        for i in range(9):
            button = tk.Button(button_frame, text=' ', font='normal 20 bold', height=2, width=5, command=lambda i=i: self.player_move(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def player_move(self, i):
        if self.buttons[i]['text'] == ' ' and not self.check_end_game():
            self.buttons[i]['text'] = 'X'
            board[i] = 'X'
            if not self.check_end_game():
                ai_index = ai_move(board, self.difficulty.get())
                self.buttons[ai_index]['text'] = 'O'
                self.check_end_game()

    def check_end_game(self):
        if check_winner(board, 'X'):
            messagebox.showinfo('Tic Tac Toe', 'You win!')
            self.reset_board()
            return True
        elif check_winner(board, 'O'):
            messagebox.showinfo('Tic Tac Toe', 'AI wins!')
            self.reset_board()
            return True
        elif check_draw(board):
            messagebox.showinfo('Tic Tac Toe', 'Draw!')
            self.reset_board()
            return True
        return False

    def reset_board(self):
        global board
        board = [' ' for _ in range(9)]
        for button in self.buttons:
            button['text'] = ' '

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
