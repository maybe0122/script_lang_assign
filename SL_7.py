from tkinter import *
import random

# 9.6 and 11.46

class MainGUI1:
    def refresh(self):
        for i in range(3):
            for j in range(3):
                x = random.randint(0, 1)
                if x:
                    self.matrix[i][j]['image'] = self.imageO
                else:
                    self.matrix[i][j]['image'] = self.imageX

    def __init__(self):
        window = Tk()
        window.title('9.6')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='pybook/image/x.gif')
        self.imageO = PhotoImage(file='pybook/image/o.gif')
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                x = random.randint(0, 1)
                self.matrix[i].append(Label(frame))
                if x:
                    self.matrix[i][j]['image'] = self.imageO
                else:
                    self.matrix[i][j]['image'] = self.imageX
                self.matrix[i][j].grid(row=i, column=j)

        frame1 = Frame(window)
        frame1.pack()
        self.label = Label(frame1)
        self.label.pack(side=LEFT)
        Button(frame1, text='다시실행', command=self.refresh).pack(side=LEFT)


        window.mainloop()


MainGUI1()


# 11.9

matrix = []

def drawBoard():
    for i in range(3):
        print('----------------')
        for j in range(3):
            print('|', matrix[i][j], ' ', end='')
        print('|')
    print('----------------')

def check():
    for i in range(3):
        player = matrix[i][0]
        if player != ' ' and player == matrix[i][1] and player == matrix[i][2]:
            return player
        player = matrix[0][i]
        if player != ' ' and player == matrix[1][i] and player == matrix[2][i]:
            return player

    player = matrix[0][0]
    if player != ' ' and player == matrix[1][1] and player == matrix[2][2]:
        return player
    player = matrix[0][2]
    if player != ' ' and player == matrix[1][1] and player == matrix[2][0]:
        return player
    return ''

def main():
    for i in range(3):
        matrix.append([])
        for j in range(3):
            matrix[i].append(' ')
    drawBoard()
    turn = True
    count = 0
    while True:
        if turn:
            row = eval(input('플레이어 x의 행(0,1, 또는 2) 입력: '))
            col = eval(input('플레이어 x의 열(0,1, 또는 2) 입력: '))
            matrix[row][col] = 'X'
        else:
            row = eval(input('플레이어 o의 행(0,1, 또는 2) 입력: '))
            col = eval(input('플레이어 o의 열(0,1, 또는 2) 입력: '))
            matrix[row][col] = 'O'
        drawBoard()
        player = check()
        if player != '':
            print('플레이어', player, '가 이겼습니다.')
            break
        turn = not turn
        if count == 9:
            print('비겼습니다.')
            break
        count += 1

main()

# 12.5

class MainGUI2:
    def check(self):
        for i in range(3):
            player = self.matrix[i][0]['text']
            if player != ' ' and player == self.matrix[i][1]['text'] and player == self.matrix[i][2]['text']:
                return player
            player = self.matrix[0][i]['text']
            if player != ' ' and player == self.matrix[1][i]['text'] and player == self.matrix[2][i]['text']:
                return player

        player = self.matrix[0][0]['text']
        if player != ' ' and player == self.matrix[1][1]['text'] and player == self.matrix[2][2]['text']:
            return player
        player = self.matrix[0][2]['text']
        if player != ' ' and player == self.matrix[1][1]['text'] and player == self.matrix[2][0]['text']:
            return player
        return ''

    def pressed(self, row, col):
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
        for i in range(3):
            for j in range(3):
                self.matrix[i][j]['image'] = self.imageE
                self.matrix[i][j]['text'] = ' '
        self.done = False
        self.explain.set('플레이어 X 차례')
        self.turn = True

    def __init__(self):
        window = Tk()
        window.title('틱택토')
        frame = Frame(window)
        frame.pack()
        self.matrix = []
        self.imageX = PhotoImage(file='pybook/image/x.gif')
        self.imageO = PhotoImage(file='pybook/image/o.gif')
        self.imageE = PhotoImage(file='pybook/image/empty.gif')
        self.turn = True
        self.done = False
        for i in range(3):
            self.matrix.append([])
            for j in range(3):
                self.matrix[i].append(Button(frame, image=self.imageE, text=' ', command=lambda row=i, col=j: self.pressed(row, col)))
                self.matrix[i][j].grid(row=i, column=j)

        frame1 = Frame(window)
        frame1.pack()
        self.explain = StringVar()
        self.explain.set("플레이어 X 차례")
        self.label = Label(frame1, textvariable=self.explain)
        self.label.pack(side=LEFT)
        Button(frame1, text='다시실행', command=self.refresh).pack(side=LEFT)


        window.mainloop()


MainGUI2()