from tkinter import *
from tkinter import font
from winsound import *
from Dori_player import *
from Dori_card import *
import random


class Dori:
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=14, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='normal', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=24, weight='bold', family='맑은 고딕')
        self.fontstyle4 = font.Font(self.window, size=12, weight='bold', family='맑은 고딕')
        self.player = [Player("player1"), Player("player2"), Player("player3")]
        self.dealer = Player("dealer")
        self.playerbetMoney = [0, 0, 0]
        self.totalMoney = 1000
        self.LcardsPlayer = [[], [], []]      # 플레이어 카드 정보 (0, 1, 2) + 1 == 플레이어
        self.LcardsDealer = []
        self.deckN = 0
        self.deal = [False, False, False]   # 배팅 여부 확인
        self.setupButton()
        self.setupLabel()
        self.window.mainloop()

    def setupButton(self):
        x = 50
        y = 550
        self.P1Bet5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressedP1Bet5)
        self.P1Bet5.place(x=x, y=y)
        self.P1Bet1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressedP1Bet1)
        self.P1Bet1.place(x=x+80, y=y)

        self.P2Bet5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressedP2Bet5)
        self.P2Bet5.place(x=x+200, y=y)
        self.P2Bet1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressedP2Bet1)
        self.P2Bet1.place(x=x+280, y=y)

        self.P3Bet5 = Button(self.window, text="5만", width=4, height=1, font=self.fontstyle2, command=self.pressedP3Bet5)
        self.P3Bet5.place(x=x+400, y=y)
        self.P3Bet1 = Button(self.window, text="1만", width=4, height=1, font=self.fontstyle2, command=self.pressedP3Bet1)
        self.P3Bet1.place(x=x+480, y=y)

        self.Deal = Button(self.window, text="Deal", width=5, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=620, y=y)
        self.Again = Button(self.window, text="Again", width=5, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=y)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    # text 위치 수정
    def setupLabel(self):
        # money label
        self.LplayerbetMoney = []
        for i in range(3):
            self.LplayerbetMoney.append(Label(text=str(self.playerbetMoney[i])+"만", width=4, height=1, font=self.fontstyle3, bg="green", fg="cyan"))
            self.LplayerbetMoney[i].place(x=100 + i * 200, y=490)

        self.LtotalMoney = Label(text=str(self.totalMoney)+"만원", width=10, height=1, font=self.fontstyle3, bg="green", fg="blue")
        self.LtotalMoney.place(x=620, y=450)

        # made label
        self.LplayerMade = []
        for i in range(3):
            self.LplayerMade.append(Label(text="", width=20, height=1, font=self.fontstyle4, bg="green", fg="cyan"))
            self.LplayerMade[i].place(x=40 + i * 200, y=290)

        self.LdealerMade = Label(text="", width=20, height=1, font=self.fontstyle4, bg="green", fg="cyan")
        self.LdealerMade.place(x=240, y=40)

        # number label
        self.Lplayer1Num = []
        for i in range(5):
            self.Lplayer1Num.append(Label(text="", width=2, height=1, font=self.fontstyle, bg="green", fg="white"))
            self.Lplayer1Num[i].place(x=70 + i * 30, y=320)

        self.Lplayer2Num = []
        for i in range(5):
            self.Lplayer2Num.append(Label(text="", width=2, height=1, font=self.fontstyle, bg="green", fg="white"))
            self.Lplayer2Num[i].place(x=270 + i * 30, y=320)

        self.Lplayer3Num = []
        for i in range(5):
            self.Lplayer3Num.append(Label(text="", width=2, height=1, font=self.fontstyle, bg="green", fg="white"))
            self.Lplayer3Num[i].place(x=470 + i * 30, y=320)

        self.LdealerNum = []
        for i in range(5):
            self.LdealerNum.append(Label(text="", width=2, height=1, font=self.fontstyle, bg="green", fg="white"))
            self.LdealerNum[i].place(x=270 + i * 30, y=70)

        # win/lose label
        self.Lplayerstatus = []
        for i in range(3):
            self.Lplayerstatus.append(Label(text="", width=4, height=1, font=self.fontstyle3, bg="green", fg="red"))
            self.Lplayerstatus[i].place(x=50 + i * 200, y=230)

    def checkBet(self):
        if self.deckN == 0:
            if False not in self.deal:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"
        else:
            if True in self.deal:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"

    def pressedP1Bet5(self):
        temp = 5
        self.playerbetMoney[0] += temp
        if self.totalMoney >= temp:
            self.LplayerbetMoney[0].configure(text=str(self.playerbetMoney[0])+"만")
            self.totalMoney -= temp
            self.LtotalMoney.configure(text=str(self.totalMoney) + "만")
            # PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.playerbetMoney[0] -= temp

        self.deal[0] = True

        self.checkBet()

    def pressedP1Bet1(self):
        temp = 1
        self.playerbetMoney[0] += temp
        if self.totalMoney >= temp:
            self.LplayerbetMoney[0].configure(text=str(self.playerbetMoney[0]) + "만")
            self.totalMoney -= temp
            self.LtotalMoney.configure(text=str(self.totalMoney) + "만")
            # PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.playerbetMoney[0] -= temp

        self.deal[0] = True

        self.checkBet()

    def pressedP2Bet5(self):
        temp = 5
        self.playerbetMoney[1] += temp
        if self.totalMoney >= temp:
            self.LplayerbetMoney[1].configure(text=str(self.playerbetMoney[1]) + "만")
            self.totalMoney -= temp
            self.LtotalMoney.configure(text=str(self.totalMoney) + "만")
            # PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.playerbetMoney[1] -= temp

        self.deal[1] = True

        self.checkBet()

    def pressedP2Bet1(self):
        temp = 1
        self.playerbetMoney[1] += temp
        if self.totalMoney >= temp:
            self.LplayerbetMoney[1].configure(text=str(self.playerbetMoney[1]) + "만")
            self.totalMoney -= temp
            self.LtotalMoney.configure(text=str(self.totalMoney) + "만")
            # PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.playerbetMoney[1] -= temp

        self.deal[1] = True

        self.checkBet()

    def pressedP3Bet5(self):
        temp = 5
        self.playerbetMoney[2] += temp
        if self.totalMoney >= temp:
            self.LplayerbetMoney[2].configure(text=str(self.playerbetMoney[2]) + "만")
            self.totalMoney -= temp
            self.LtotalMoney.configure(text=str(self.totalMoney) + "만")
            # PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.playerbetMoney[2] -= temp

        self.deal[2] = True

        self.checkBet()

    def pressedP3Bet1(self):
        temp = 1
        self.playerbetMoney[2] += temp
        if self.totalMoney >= temp:
            self.LplayerbetMoney[2].configure(text=str(self.playerbetMoney[2]) + "만")
            self.totalMoney -= temp
            self.LtotalMoney.configure(text=str(self.totalMoney) + "만")
            # PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.playerbetMoney[2] -= temp

        self.deal[2] = True

        self.checkBet()

    def init_deal(self):
        for i in range(3):
            self.player[i].reset()
        self.dealer.reset()

        # 카드 덱 40장 셔플링 0,1,,.39
        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer1(0)
        self.hitPlayer2(0)
        self.hitPlayer3(0)
        self.hitDealer(0)

    def hitPlayer1(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player[0].addCard(newCard)
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        self.LcardsPlayer[0].append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[0][self.player[0].inHand() - 1].image = p

        self.LcardsPlayer[0][self.player[0].inHand() - 1].place(x=50 + n * 30, y=350)

        self.Lplayer1Num[n].configure(text=str(newCard.month))

        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer2(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player[1].addCard(newCard)
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        self.LcardsPlayer[1].append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[1][self.player[1].inHand() - 1].image = p

        self.LcardsPlayer[1][self.player[1].inHand() - 1].place(x=250 + n * 30, y=350)

        self.Lplayer2Num[n].configure(text=str(newCard.month))

        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer3(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player[2].addCard(newCard)
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        self.LcardsPlayer[2].append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[2][self.player[2].inHand() - 1].image = p

        self.LcardsPlayer[2][self.player[2].inHand() - 1].place(x=450 + n * 30, y=350)

        self.Lplayer3Num[n].configure(text=str(newCard.month))

        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self, n):                 # 수정 o
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.dealer.addCard(newCard)
        # test
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        # p = PhotoImage(file="../GodoriCards/cardback.gif")
        self.LcardsDealer.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[self.dealer.inHand() - 1].image = p

        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=100)

        self.LdealerNum[n].configure(text=str(newCard.month))

        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def pressedDeal(self):  # 수정 o
        # self.deal 초기화
        for i in range(3):
            self.deal[i] = False

        if self.deckN == 0:
            self.init_deal()
        elif self.deckN == 4:
            for i in range(1, 3 + 1):
                self.hitPlayer1(i)
                self.hitPlayer2(i)
                self.hitPlayer3(i)
                self.hitDealer(i)
        elif self.deckN == 16:
            self.hitPlayer1(4)
            self.hitPlayer2(4)
            self.hitPlayer3(4)
            self.hitDealer(4)
            self.checkWinner()

        # PlaySound('../sounds/ding.wav', SND_FILENAME)

        self.Deal["state"] = "disabled"
        self.Deal["bg"] = "gray"

    def pressedAgain(self):      # 수정 o
        for i in range(5):
            self.LcardsDealer[i].destroy()
            for j in range(3):
                self.LcardsPlayer[j][i].destroy()

        self.LcardsDealer.clear()
        self.LcardsPlayer = [[], [], []]

        for i in range(3):
            self.player[i].reset()
            self.playerbetMoney[i] = 0
            self.LplayerbetMoney[i].configure(text=str(self.playerbetMoney[i])+"만")
        self.dealer.reset()

        self.deckN = 0

        for i in range(5):
            self.Lplayer1Num[i].configure(text="", fg='white')
            self.Lplayer2Num[i].configure(text="", fg='white')
            self.Lplayer3Num[i].configure(text="", fg='white')
            self.LdealerNum[i].configure(text="", fg='white')

        for i in range(3):
            self.Lplayerstatus[i].configure(text='')
            self.LplayerMade[i].configure(text='')
            self.LdealerMade.configure(text='')

        # self.deal 초기화
        for i in range(3):
            self.deal[i] = False

        # 버튼 초기화
        self.P1Bet5['state'] = 'active'
        self.P1Bet5['bg'] = 'white'

        self.P1Bet1['state'] = 'active'
        self.P1Bet1['bg'] = 'white'

        self.P2Bet5['state'] = 'active'
        self.P2Bet5['bg'] = 'white'
        self.P2Bet1['state'] = 'active'
        self.P2Bet1['bg'] = 'white'

        self.P3Bet5['state'] = 'active'
        self.P3Bet5['bg'] = 'white'
        self.P3Bet1['state'] = 'active'
        self.P3Bet1['bg'] = 'white'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def checkWinner(self):
        # check winner
        n = [False, False, False]
        w = [False, False, False]
        check_list = [self.dealer.made()]
        for i in range(3):
            check_list.append(self.player[i].made())

        print(check_list)

        if check_list[0][0] == -1:      # dealer no made
            self.LdealerMade.configure(text=check_list[0][1])
        else:
            self.LdealerMade.configure(text=check_list[0][1])
            for i in check_list[0][2]:
                self.LdealerNum[i].configure(fg='yellow')
                self.LcardsDealer[i].place(y=120)

        for i in range(1, 3 + 1):
            if check_list[i][0] == -1:
                self.LplayerMade[i-1].configure(text=check_list[i][1])
                self.Lplayerstatus[i - 1].configure(text="패")
                n[i-1] = False
            else:
                n[i-1] = True
                if check_list[0][0] >= check_list[i][0]:    # 패
                    self.LplayerMade[i-1].configure(text=check_list[i][1])
                    self.Lplayerstatus[i-1].configure(text="패")
                else:   # 승
                    self.LplayerMade[i - 1].configure(text=check_list[i][1])
                    self.Lplayerstatus[i - 1].configure(text="승")
                    w[i-1] = True
                    self.totalMoney += self.playerbetMoney[i-1] * 2

        if n[0]:
            for i in check_list[1][2]:
                self.Lplayer1Num[i].configure(fg='yellow')
                self.LcardsPlayer[0][i].place(y=370)
        if n[1]:
            for i in check_list[2][2]:
                self.Lplayer2Num[i].configure(fg='yellow')
                self.LcardsPlayer[1][i].place(y=370)
        if n[2]:
            for i in check_list[3][2]:
                self.Lplayer3Num[i].configure(fg='yellow')
                self.LcardsPlayer[2][i].place(y=370)

        # 버튼 비활성화
        self.LtotalMoney.configure(text=str(self.totalMoney)+"만")
        self.P1Bet5['state'] = 'disabled'
        self.P1Bet5['bg'] = 'gray'
        self.P1Bet1['state'] = 'disabled'
        self.P1Bet1['bg'] = 'gray'

        self.P2Bet5['state'] = 'disabled'
        self.P2Bet5['bg'] = 'gray'
        self.P2Bet1['state'] = 'disabled'
        self.P2Bet1['bg'] = 'gray'

        self.P3Bet5['state'] = 'disabled'
        self.P3Bet5['bg'] = 'gray'
        self.P3Bet1['state'] = 'disabled'
        self.P3Bet1['bg'] = 'gray'

        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

        # if True in w:
        #     PlaySound('../sounds/win.wav', SND_FILENAME)
        # else:
        #     PlaySound('../sounds/wrong.wav', SND_FILENAME)


Dori()
