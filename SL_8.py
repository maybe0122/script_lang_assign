from tkinter import *

# 11-20
matrix = []

def drawBoard():
    print('------------------------------------')
    for i in range(6):
        for j in range(7):
            print('|', matrix[i][j], ' ', end='')
        print('|')
        print('------------------------------------')

def check():
    for i in range(6):
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i][j+1] and player == matrix[i][j+2] and player == matrix[i][j+3]:
                return player

    for i in range(3):
        for j in range(7):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j] and player == matrix[i+2][j] and player == matrix[i+3][j]:
                return player

    for i in range(3):
        for j in range(4):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j+1] and player == matrix[i+2][j+2] and player == matrix[i+3][j+3]:
                return player

    for i in range(3):
        for j in range(3, 7):
            player = matrix[i][j]
            if player != ' ' and player == matrix[i+1][j-1] and player == matrix[i+2][j-2] and player == matrix[i+3][j-3]:
                return player
    return ''

def findRow(col):
    for row in range(5, -1, -1):
        if matrix[row][col] == ' ':
            return row
    return 6

def main11_20():
    for i in range(6):
        matrix.append([])
        for j in range(7):
            matrix[i].append(' ')
    drawBoard()
    turn = True
    count = 0
    while True:
        count += 1
        if count == 43:
            print('무승부 입니다.')
            break
        if turn:
            col = eval(input('열 0-6에 빨간색 디스크를 떨어뜨리세요: '))
        else:
            col = eval(input('열 0-6에 노란색 디스크를 떨어뜨리세요: '))

        if col < 0 or col > 6:
            print('범위 내의 숫자를 입력해주세요')
            drawBoard()
            continue

        row = findRow(col)
        while True:
            if row != 6:
                if turn:
                    matrix[row][col] = 'R'
                else:
                    matrix[row][col] = 'L'
                break
            else:
                print('꽉 찬 열입니다. 다시 떨어뜨리세요')
                turn = not turn
                break
        drawBoard()
        player = check()
        if player != '':
            if player == 'R':
                print('빨간색 플레이어가 이겼습니다.')
            else:
                print('노란색 플레이어가 이겼습니다.')
            break
        turn = not turn


main11_20()


# 12-13

class MainGUI:
    def check(self):
        for i in range(6):
            for j in range(4):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i][j + 1]['text'] and \
                        player == self.matrix[i][j + 2]['text'] and \
                        player == self.matrix[i][j + 3]['text']:
                    return player

        for i in range(3):
            for j in range(7):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j]['text'] and \
                        player == self.matrix[i + 2][j]['text'] and \
                        player == self.matrix[i + 3][j]['text']:
                    return player

        for i in range(3):
            for j in range(4):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j + 1]['text'] and \
                        player == self.matrix[i + 2][j + 2]['text'] and \
                        player == self.matrix[i + 3][j + 3]['text']:
                    return player

        for i in range(3):
            for j in range(3, 7):
                player = self.matrix[i][j]['text']
                if player != ' ' and player == self.matrix[i + 1][j - 1]['text'] and \
                        player == self.matrix[i + 2][j - 2]['text'] and \
                        player == self.matrix[i + 3][j - 3]['text']:
                    return player
        return ''

    def findRow(self, col):
        for row in range(5, -1, -1):
            if self.matrix[row][col]['text'] == ' ':
                return row
        return 6

    def pressed(self, col):
        row = self.findRow(col)
        if not self.done and self.matrix[row][col]['text'] == ' ':
            if self.turn:
                self.matrix[row][col]['image'] = self.imageX
                self.matrix[row][col]['text'] = 'X'
            else:
                self.matrix[row][col]['image'] = self.imageO
                self.matrix[row][col]['text'] = 'O'
            self.turn = not self.turn
            if self.check() != '':
                self.done = True
                self.explain.set('플레이어'+self.check()+'이겼습니다.')
            elif self.turn:
                self.explain.set('플레이어 X 차례')
            else:
                self.explain.set('플레이어 O 차례')

    def refresh(self):
        for i in range(6):
            for j in range(7):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set('플레이어 X 차례')
        self.turn = True

    def __init__(self):
        window = Tk()
        window.title('사목게임')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='pybook/image/x.gif')
        self.imageO = PhotoImage(file='pybook/image/o.gif')
        self.imageE = PhotoImage(file='pybook/image/empty.gif')
        self.turn = True
        self.done = False
        self.count = 0
        for i in range(6):
            self.matrix.append([])
            for j in range(7):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ',
                                             command=lambda col=j: self.pressed(col)))
                self.matrix[i][j].grid(row=i, column=j)

        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("플레이어 X 차례")
        self.label = Label(frame1, textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1, text='다시실행', command=self.refresh).pack(side=LEFT)

        window.mainloop()


MainGUI()