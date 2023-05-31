from tkinter import *
from tkinter import messagebox
import random

class Game2048:
    # 숫자 배경 색 사전
    bg_color = {
        2: '#eee4da', 4: '#ede0c8', 8: '#edc850',
        16: '#edc53f', 32: '#f67c5f', 64: '#f65e3b',
        128: '#edcf72', 256: '#edcc61', 512: '#f2b179',
        1024: '#f59563', 2048: '#edc22e', }

    # 숫자 색 사전
    color = {
    2: '#776e65', 4: '#f9f6f2', 8: '#f9f6f2',
    16: '#f9f6f2', 32: '#f9f6f2', 64: '#f9f6f2',
    128: '#f9f6f2', 256: '#f9f6f2', 512: '#776e65',
    1024: '#f9f6f2', 2048: '#f9f6f2', }

    def __init__(self, size):
        self.n = size

        self.window = Tk()
        self.window.title('2048 Game')
        self.gameArea = Frame(self.window, bg='azure3')
        self.gridCell = [[0] * self.n for _ in range(self.n)]
        self.compress = False
        self.merge = False
        self.moved = False
        self.end = False
        self.won = False
        self.score = 0
        self.board = []

        for r in range(self.n):
            rows = []
            for c in range(self.n):
                l = Label(self.gameArea, text='', bg='azure4', font=('arial', 22, 'bold'), width=4, height=2)
                l.grid(row=r, column=c, padx=7, pady=7)
                rows.append(l)
            self.board.append(rows)
        self.gameArea.pack()
        self.random_cell()
        self.random_cell()
        self.paintGrid()
        self.window.bind('<Key>', self.link_keys)
        self.window.mainloop()

    def link_keys(self, event):
        if self.end or self.won:
            return
        self.compress = False
        self.merge = False
        self.moved = False
        key = event.keysym
        if key == 'Up':     # 수정
            self.compress_up()
            self.mergeCol()
            self.moved = self.compress or self.merge
            self.compress_up()
        elif key == 'Down':     # 수정
            self.compress_down()
            self.mergeCol()
            self.moved = self.compress or self.merge
            self.compress_down()
        elif key == 'Left':
            self.compress_left()
            self.mergeRow()
            self.moved = self.compress or self.merge
            self.compress_left()
        elif key == 'Right':    # 수정
            self.compress_right()
            self.mergeRow()
            self.moved = self.compress or self.merge
            self.compress_right()
        else:
            pass

        self.paintGrid()

        flag = 0
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 2048:
                    flag = 1
                    break

        if flag == 1:
            self.won = True
            messagebox.showinfo('2048', 'Yon won!!')
            return

        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    flag = 1
                    break
        if not (flag or self.can_merge()):
            self.end = True
            messagebox.showinfo('2048', 'Game Over!!')
        if self.moved:
            self.random_cell()
        self.paintGrid()

    def random_cell(self):
        cells = []

        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    cells.append((r, c))
        curr = random.choice(cells)
        (r, c) = curr
        self.gridCell[r][c] = 2

    def paintGrid(self):
        for r in range(self.n):
            for c in range(self.n):
                if self.gridCell[r][c] == 0:
                    self.board[r][c].configure(text='', bg='azure4')

                else:
                    self.board[r][c].configure(text=str(self.gridCell[r][c]),
                               bg=self.bg_color[self.gridCell[r][c]],
                               fg=self.color[self.gridCell[r][c]])

    def compress_left(self):
        self.compress = False

        temp = [[0] * self.n for _ in range(self.n)]
        for r in range(self.n):
            cnt = 0
            for c in range(self.n):
                if self.gridCell[r][c] != 0:
                    temp[r][cnt] = self.gridCell[r][c]
                    if cnt != c:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def compress_right(self):       # 수정
        self.compress = False

        temp = [[0] * self.n for _ in range(self.n)]
        for r in range(self.n):
            cnt = self.n - 1
            for c in range(self.n - 1, -1, -1):
                if self.gridCell[r][c] != 0:
                    temp[r][cnt] = self.gridCell[r][c]
                    if cnt != c:
                        self.compress = True
                    cnt -= 1
        self.gridCell = temp

    def compress_up(self):          # 수정
        self.compress = False

        temp = [[0] * self.n for _ in range(self.n)]
        for c in range(self.n):
            cnt = 0
            for r in range(self.n):
                if self.gridCell[r][c] != 0:
                    temp[cnt][c] = self.gridCell[r][c]
                    if cnt != r:
                        self.compress = True
                    cnt += 1
        self.gridCell = temp

    def compress_down(self):        # 수정
        self.compress = False

        temp = [[0] * self.n for _ in range(self.n)]
        for c in range(self.n):
            cnt = self.n - 1
            for r in range(self.n - 1, -1, -1):
                if self.gridCell[r][c] != 0:
                    temp[cnt][c] = self.gridCell[r][c]
                    if cnt != r:
                        self.compress = True
                    cnt -= 1
        self.gridCell = temp

    def mergeRow(self):
        self.merge = False

        for r in range(self.n):
            for c in range(self.n - 1):
                if self.gridCell[r][c] != 0 and self.gridCell[r][c] == self.gridCell[r][c + 1]:
                    self.gridCell[r][c] *= 2
                    self.gridCell[r][c + 1] = 0
                    self.score += self.gridCell[r][c]
                    self.merge = True

    def mergeCol(self):             # 수정
        self.merge = False

        for c in range(self.n):
            for r in range(self.n - 1):
                if self.gridCell[r][c] != 0 and self.gridCell[r][c] == self.gridCell[r+1][c]:
                    self.gridCell[r][c] *= 2
                    self.gridCell[r+1][c] = 0
                    self.score += self.gridCell[r][c]
                    self.merge = True

    def can_merge(self):    # 수정
        # 합칠게 남아 있는 지 검사

        for r in range(self.n):
            for c in range(self.n - 1):
                if self.gridCell[r][c] == self.gridCell[r][c + 1]:
                    return True

        for c in range(self.n):
            for r in range(self.n - 1):
                if self.gridCell[r][c] == self.gridCell[r+1][c]:
                    return True


Game2048(4)
