from tkinter import *
from random import *
import tkinter.simpledialog as sl


# 9.1 수정 필요
class MainGUI9_1:
    def up(self):
        if self.y > 0:
            self.canvas.move('ball', 0, - 5)
            self.y -= 5

    def down(self):
        if self.y + 5 < self.height:
            self.canvas.move('ball', 0, 5)
            self.y += 5

    def left(self):
        if self.x > 0:
            self.canvas.move('ball', -5, 0)
            self.x -= 5

    def right(self):
        if self.x + 5 < self.width:
            self.canvas.move('ball', 5, 0)
            self.x += 5

    def __init__(self):
        window = Tk()
        window.title("공 옮기기")
        self.width = 200
        self.height = 100
        self.x = 10
        self.y = 10
        self.canvas = Canvas(window, bg="white", width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.create_oval(10, 10, 20, 20, fill='red', tags='ball')
        frame = Frame(window)
        frame.pack()
        Button(frame, text='상', command=self.up).pack(side=LEFT)
        Button(frame, text='하', command=self.down).pack(side=LEFT)
        Button(frame, text='좌', command=self.left).pack(side=LEFT)
        Button(frame, text='우', command=self.right).pack(side=LEFT)

        window.mainloop()

MainGUI9_1()

# 9.2
class MainGUI9_2:
    def compute(self):
        mRate = float(self.rate.get()) / 1200
        f = float(self.money.get()) * (1+mRate)**(float(self.years.get())*12)
        self.futureValue.set(f'{f:.2f}')

    def __init__(self):
        window = Tk()
        window.title("투자금 계산")
        Label(window, text='투자금').grid(row=1, column=1, sticky=W)
        Label(window, text='기간').grid(row=2, column=1, sticky=W)
        Label(window, text='연이율').grid(row=3, column=1, sticky=W)
        Label(window, text='미래가치').grid(row=4, column=1, sticky=W)
        self.money = StringVar()
        Entry(window, textvariable=self.money, justify=RIGHT).grid(row=1, column=2)
        self.years = StringVar()
        Entry(window, textvariable=self.years, justify=RIGHT).grid(row=2, column=2)
        self.rate = StringVar()
        Entry(window, textvariable=self.rate, justify=RIGHT).grid(row=3, column=2)
        self.futureValue = StringVar()
        Label(window, textvariable=self.futureValue).grid(row=4, column=2, sticky=E)

        Button(window, text='계산하기', command=self.compute).grid(row=5, column=2, sticky=E)


        window.mainloop()

MainGUI9_2()

# 9.3
class MainGUI9_3:
    def display(self):
        self.canvas.delete('shape')
        if self.filled.get() == 1:
            if self.v.get() == 1:
                self.canvas.create_rectangle(self.width / 2 - self.width * 0.4, self.height / 2 - self.height * 0.4,
                                             self.width / 2 + self.width * 0.4, self.height / 2 + self.height * 0.4,
                                             fill='red', tags='shape')
            else:
                self.canvas.create_oval(self.width / 2 - self.width * 0.4, self.height / 2 - self.height * 0.4,
                                             self.width / 2 + self.width * 0.4, self.height / 2 + self.height * 0.4,
                                             fill='red', tags='shape')
        else:
            if self.v.get() == 1:
                self.canvas.create_rectangle(self.width / 2 - self.width * 0.4, self.height / 2 - self.height * 0.4,
                                             self.width / 2 + self.width * 0.4, self.height / 2 + self.height * 0.4,
                                             tags='shape')
            else:
                self.canvas.create_oval(self.width / 2 - self.width * 0.4, self.height / 2 - self.height * 0.4,
                                             self.width / 2 + self.width * 0.4, self.height / 2 + self.height * 0.4,
                                             tags='shape')
    def __init__(self):
        window = Tk()
        window.title('라디오버튼과 체크 버튼')
        self.width = 300
        self.height = 50
        self.canvas = Canvas(window, bg='white', width=self.width, height=self.height)
        self.canvas.create_rectangle(self.width/2-self.width*0.4, self.height/2-self.height*0.4,
                                     self.width/2+self.width*0.4, self.height/2+self.height*0.4, tags='shape')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.v = IntVar()
        Radiobutton(frame, text='직사각형', variable=self.v, value=1, command=self.display).pack(side=LEFT)
        Radiobutton(frame, text='타원', variable=self.v, value=2, command=self.display).pack(side=LEFT)
        self.filled = IntVar()
        Checkbutton(frame, text='채우기', variable=self.filled, command=self.display).pack(side=LEFT)
        window.mainloop()

MainGUI9_3()

# 10.33
class Ball:
    def toHexChar(self, value):
        if 0 <= value <= 9:
            return chr(value+ord('0'))
        else:
            return chr(value-10+ord('A'))

    def getRandomColor(self):
        color = '#'
        for i in range(6):
            color += self.toHexChar(randint(0, 15))
        return color

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 2
        self.dy = 2
        self.color = self.getRandomColor()

class MainGUI10_3:
    def stop(self):
        self.isStopped = True

    def resume(self):
        self.isStopped = False
        self.animate()

    def add(self):
        self.balllist.append(Ball())

    def remove(self):
        self.balllist.pop()

    def faster(self):
        if self.sleepTime > 20:
            self.sleepTime -= 20

    def slower(self):
        self.sleepTime += 20

    def animate(self):
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete('ball')
            for ball in self.balllist:
                self.displayBall(ball)

    def displayBall(self, ball):
        if ball.x >= self.width:
            ball.dx = -2
        elif ball.x < 0:
            ball.dx = 2
        if ball.y >= self.height:
            ball.dy = -2
        elif ball.y < 0:
            ball.dy = 2
        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x-3, ball.y-3, ball.x+3, ball.y+3, fill=ball.color, tags='ball')


    def __init__(self):
        window = Tk()
        window.title('공 튕기기')
        self.balllist = []
        self.isStopped = False
        self.width = 800
        self.height = 600
        self.sleepTime = 100
        self.canvas = Canvas(window, bg='white', width=self.width, height=self.height)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame, text='정지', command=self.stop).pack(side=LEFT)
        Button(frame, text='재시작', command=self.resume).pack(side=LEFT)
        Button(frame, text='+', command=self.add).pack(side=LEFT)
        Button(frame, text='-', command=self.remove).pack(side=LEFT)
        Button(frame, text='빠르게', command=self.faster).pack(side=LEFT)
        Button(frame, text='느리게', command=self.slower).pack(side=LEFT)
        self.animate()
        window.mainloop()

MainGUI10_3()

# 10.35
class MainGUI10_35:
    def display(self):
        self.canvas.delete('histogram')
        counts = [0]*26
        for i in range(1000):
            ch = randint(0, 25)
            counts[ch] += 1
        barWidth = (self.width-20)/26
        maxCount = max(counts)
        for i in range(26):
            self.canvas.create_rectangle(10+i*barWidth, self.height-(self.height-10)*counts[i]/maxCount,
                                         10+(i+1)*barWidth, self.height-10, tags='histogram')
            self.canvas.create_text(10+i*barWidth + 15, self.height-5, text=chr(i+ord('a')), tags='histogram')
            self.canvas.create_text(10+i*barWidth + 15, self.height-(self.height-10)*counts[i]/maxCount-5,
                                    text=str(counts[i]), tags='histogram')

    def __init__(self):
        self.width = 800
        self.height = 600
        window = Tk()
        window.title('문자의 개수 세기')
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        Button(window, text='히스토그램 출력', command=self.display).pack()
        window.mainloop()

MainGUI10_35()

# 10.36
class MainGUI10_36:
    def reGen(self):
        self.canvas.delete('histogram')
        self.canvas.delete('current_bar')
        self.counts = [x for x in range(1, 21)]
        shuffle(self.counts)
        self.current = 0
        self.barWidth = (self.width-20)/20
        self.maxCount = max(self.counts)
        for i in range(20):
            self.canvas.create_rectangle(10+i*self.barWidth, self.height-(self.height-10)*self.counts[i]/self.maxCount,
                                         10+(i+1)*self.barWidth, self.height-10, tags='histogram')

            self.canvas.create_text(10+i*self.barWidth + 20, self.height-(self.height-10)*self.counts[i]/self.maxCount-5
                                    , text=str(self.counts[i]), tags='histogram')

    def next(self):
        key = int(self.key.get())
        self.canvas.delete('current_bar')

        self.canvas.create_rectangle(10 + self.current * self.barWidth,
                                     self.height - (self.height - 10) * self.counts[self.current] / self.maxCount,
                                     10 + (self.current + 1) * self.barWidth, self.height - 10, fill='red',
                                     tags='current_bar')
        if key == self.counts[self.current]:
            sl.messagebox.showinfo('찾았다', f'{key}')
        else:
            self.current += 1

    def __init__(self):
        self.width = 800
        self.height = 600
        window = Tk()
        window.title('선형 검색 애니메이션')
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Label(frame, text='키를 입력하세요: ').pack(side=LEFT)
        self.key = IntVar()
        Entry(frame, textvariable=self.key, justify=RIGHT, width=3).pack(side=LEFT)
        Button(frame, text='다음단계', command=self.next).pack(side=LEFT)
        Button(frame, text='재설정', command=self.reGen).pack(side=LEFT)

        window.mainloop()

MainGUI10_36()

# 10.38
class MainGUI10_38:
    def reGen(self):
        self.canvas.delete('histogram')
        # self.canvas.delete('current_bar')
        self.counts = [x for x in range(1, 21)]
        shuffle(self.counts)
        self.current = 0
        self.barWidth = (self.width-20)/20
        self.maxCount = max(self.counts)
        for i in range(20):
            self.canvas.create_rectangle(10+i*self.barWidth, self.height-(self.height-10)*self.counts[i]/self.maxCount,
                                         10+(i+1)*self.barWidth, self.height-10, tags='histogram')

            self.canvas.create_text(10+i*self.barWidth + 20, self.height-(self.height-10)*self.counts[i]/self.maxCount-5
                                    , text=str(self.counts[i]), tags='histogram')

    def next(self):
        if self.current < 20:
            indexMin = self.current
            for i in range(self.current+1, 20):
                if self.counts[indexMin] > self.counts[i]:
                    indexMin = i
            self.counts[self.current], self.counts[indexMin] = self.counts[indexMin], self.counts[self.current]

            self.canvas.delete('current_bar')
            self.canvas.delete('histogram')
            for i in range(20):
                self.canvas.create_rectangle(10 + i * self.barWidth,
                                             self.height - (self.height - 10) * self.counts[i] / self.maxCount,
                                             10 + (i + 1) * self.barWidth, self.height - 10, tags='histogram')

                self.canvas.create_text(10 + i * self.barWidth + 20,
                                        self.height - (self.height - 10) * self.counts[i] / self.maxCount - 5
                                        , text=str(self.counts[i]), tags='histogram')

            self.canvas.create_rectangle(10 + self.current * self.barWidth,
                                        self.height - (self.height - 10) * self.counts[self.current] / self.maxCount,
                                        10 + (self.current + 1) * self.barWidth, self.height - 10, fill='red',
                                        tags='histogram')
            self.current += 1

    def __init__(self):
        self.width = 800
        self.height = 600
        self.current = 0
        window = Tk()
        window.title('선택 정렬 애니메이션')
        self.canvas = Canvas(window, width=self.width, height=self.height, bg='white')
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        Button(frame, text='다음단계', command=self.next).pack(side=LEFT)
        Button(frame, text='재설정', command=self.reGen).pack(side=LEFT)

        window.mainloop()

MainGUI10_38()

# 10.39
class MainGUI10_39:
    def refresh(self):
        shuffle(self.index)
        for i in range(4):
            self.labelList[i]['image'] = self.imageList[self.index[i]]

    def check(self):
        fourCards = []
        for i in range(4):
            fourCards.append(self.index[i] % 13)
        fourCards.sort()
        fourCards = [x+1 for x in fourCards]
        ex = self.answer.get()
        ex = ex.replace('+', ' ')
        ex = ex.replace('-', ' ')
        ex = ex.replace('/', ' ')
        ex = ex.replace('*', ' ')
        ex = ex.replace('(', ' ')
        ex = ex.replace(')', ' ')
        numbers = ex.split()
        numbers = [eval(x) for x in numbers]
        numbers.sort()
        if fourCards == numbers:
            if eval(self.answer.get()) == 24:
                sl.messagebox.showinfo('정확', '맞았습니다.')
            else:
                sl.messagebox.showerror('틀림', self.answer.get()+'는 24가 아닙니다.')
        else:
            sl.messagebox.showerror('틀림', '보여지는 카드를 사용해야 됩니다.')


    def __init__(self):
        window = Tk()
        window.title('24점 게임')
        self.index = [x for x in range(52)]
        self.imageList=[]
        for i in range(1, 53):
            self.imageList.append(PhotoImage(file='card/'+str(i)+'.gif'))
        frame1 = Frame(window)
        frame1.pack()
        Button(frame1, text='새로고침',command=self.refresh).pack()
        frame2 = Frame(window)
        frame2.pack()
        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame2, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)
        self.refresh()
        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text='수식을 입력하세요:').pack(side=LEFT)
        self.answer = StringVar()
        Entry(frame3, textvariable=self.answer).pack(side=LEFT)
        Button(frame3, text='확인', command=self.check).pack(side=LEFT)

        window.mainloop()

MainGUI10_39()
