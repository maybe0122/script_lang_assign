# 7.1(rectangle class)
class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height
    def getArea(self):
        return self.width * self.height
    def getPerimter(self):
        return (self.width+self.height) * 2
    def info(self):
        print(f'width: {self.width}, height: {self.height}, area: {self.getArea():.2f}, perimeter: {self.getPerimter()}')

print('7-1')
r1 = Rectangle(4, 40)
r1.info()
r2 = Rectangle(3.5, 35.9)
r2.info()
print()

# 7.2(stock class)
class Stock:
    def __init__(self, name, symbol, previousPrice, currentPrice):
        self.__name = name
        self.__symbol = symbol
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousPrice

    def setPreviousPrice(self, value):
        self.__previousPrice = value

    def getCurrentPrice(self):
        return self.__currentPrice

    def setCurrentPrice(self, value):
        self.__currentPrice = value

    def getChangePercent(self):
        return '{0:.2f}%'.format(100 * ((self.__currentPrice - self.__previousPrice) / self.__previousPrice))

print('7-2')
stock = Stock("intel", "INTC", 20500, 20350)
print("가격 변화율 %: ", stock.getChangePercent())
print()
# 7.4 (fan class)
SLOW = 1
MEDIUM = 2
FAST = 3
class Fan:
    def __init__(self, speed=SLOW, radius=5, color='blue', on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    def getSpeed(self):
        return self.__speed
    def setSpeed(self, value):
        self.__speed = value
    def getRadius(self):
        return self.__radius
    def setRadius(self, value):
        self.__radius  = value
    def getColor(self):
        return self.__color
    def setColor(self, value):
        self.__color = value
    def getOn(self):
        return self.__on
    def setOn(self, value):
        self.__on = value


def display(fan):
    print(f'speed: {fan.getSpeed()}, color: {fan.getColor()}, radius: {fan.getRadius()}, on: {fan.getOn()}')

print('7-4')
fan1 = Fan(FAST, 10, 'yellow', True)
fan2 = Fan(MEDIUM, 5, 'blue', False)
display(fan1)
display(fan2)
print()

# 7.8 (stopwatch)
import time
class StopWatch:
    def __init__(self):
        self.__startTime = time.time()
    def getStartTime(self):
        return self.__startTime
    def getEndTime(self):
        return self.__endTime
    def start(self):
        self.__startTime = time.time()
    def stop(self):
        self.__endTime = time.time()
    def getElapsedTime(self):
        return int((self.__endTime - self.__startTime) * 1000)

print('7-8')
s = StopWatch()
sum = 0
for i in range(1000000):
    sum += i
s.stop()
print('1부터 1000000까지 더하는 데 걸리는 밀리초: ', s.getElapsedTime())
print()

# 12.1 (triangle class)
class GeometricObject:
    def __init__(self,color='blue',filled=True):
        self.color = color
        self.filled = filled
class Triangle(GeometricObject):
    def __init__(self,side1=1, side2=1, side3=1):
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def __str__(self):
        return 'Triangle: side1 = ' + str(self.side1) + 'side2 = ' + str(self.side2) + 'side3 = ' + str(self.side3)
    def info(self):
        print(f'color:{self.color},filled:{self.filled},area:{self.getArea():.2f},perimeter:{self.getPerimeter()}')

print('12-1')
t = Triangle(10,20,25)
t.filled = True
t.color = 'yellow'
t.info()
print(t)
print()

# 13.1 (remove text)
print('14-1')
f = input("파일 이름을 입력하세요: ")
infile = open(f, 'r')
s = infile.read()
removeString = input('제거할 문자열을 입력하세요: ')
newS = s.replace(removeString, '')
infile.close()
outfile = open(f, 'w')
print(newS, file=outfile, end='')
print('완료')
outfile.close()
print()

# 13.2 (count char)
print('13-2')
f = input("파일 이름을 입력하세요: ")
infile = open(f, 'r')
s = infile.read()
print('문자', str(len(s)), '개')
print('단어', str(len(s.split())), '개')
print('행', str(len(s.split('\n'))), '개')
infile.close()
print()

# # 14.4 (Tkinter: text widget)
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
def openFile():
    fn = askopenfilename()
    filename.set(fn)

def showResult():
    fn = filename.get()
    try:
        infile = open(fn, 'r')
        counts = [0]*26
        for line in infile:
            lowerLine = line.lower()
            for ch in lowerLine:
                if ch.isalpha():
                    counts[ord(ch)-ord('a')] += 1
        for i in range(26):
            if counts[i] != 0:
                text.insert(END, chr(i+ord('a'))+ '-' +str(counts[i])+ '번 나타납니다.\n')
        infile.close()
    except IOError:
        tkinter.messagebox.showwarning(fn+' 파일이 존재하지 않습니다')
window = Tk()
window.title('문자의 출현 빈도수')
frame1 = Frame(window)
frame1.pack()
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD, yscrollcommand= Scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)
frame2 = Frame(window)
frame2.pack()
Label(frame2, text='파일명을 입력하세요:').pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable= filename).pack(side=LEFT)
Button(frame2, text='열기',command=openFile).pack(side=LEFT)
Button(frame2, text='결과보기',command=showResult).pack(side=LEFT)
window.mainloop()



# 14.7 (Tkinter: graph widget)
def openFile():
    fn = askopenfilename()
    filename.set(fn)

def showResult2():
    fn = filename.get()
    try:
        infile = open(fn, 'r')
        counts = [0] * 26
        for line in infile:
            lowerLine = line.lower()
            for ch in lowerLine:
                if ch.isalpha():
                    counts[ord(ch) - ord('a')] += 1
        width = int(canvas['width'])
        height = int(canvas['height'])
        maxCounts = max(counts)
        heightBar = height*0.75
        widthBar = width - 20
        for i in range(26):
            canvas.create_rectangle(i * widthBar / 26 + 10, height - heightBar * counts[i] / maxCounts - 20,
                                    (i + 1) * widthBar / 26, height - 20)
            canvas.create_text(i*widthBar/26 + 10 + 0.5*widthBar/26, height-10, text=chr(i+ord('a')))
        infile.close()
    except IOError:
        tkinter.messagebox.showwarning(fn + ' 파일이 존재하지 않습니다')

window = Tk()
window.title('문자의 출현 빈도수')
frame1 = Frame(window)
frame1.pack()
canvas = Canvas(frame1, width=500, height=200)
canvas.pack()
frame2 = Frame(window)
frame2.pack()
Label(frame2, text='파일명을 입력하세요:').pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable= filename).pack(side=LEFT)
Button(frame2, text='열기',command=openFile).pack(side=LEFT)
Button(frame2, text='결과보기',command=showResult2).pack(side=LEFT)
window.mainloop()