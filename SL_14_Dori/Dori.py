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
        self.fontstyle = font.Font(self.window, size=12, weight='normal', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='normal', family='Consolas')
        self.fontstyle3 = font.Font(self.window, size=24, weight='normal', family='Consolas')
        self.player1 = Player("player1")
        self.player2 = Player("player2")
        self.player3 = Player("player3")
        self.dealer = Player("dealer")
        self.P1betMoney = 0
        self.P2betMoney = 0
        self.P3betMoney = 0
        self.totalMoney = 1000
        self.nCardsDealer = 0
        self.nCardsPlayer1 = 0
        self.nCardsPlayer2 = 0
        self.nCardsPlayer3 = 0
        self.LcardsPlayer1 = []
        self.LcardsPlayer2 = []
        self.LcardsPlayer3 = []
        self.LcardsDealer = []
        self.deckN = 0
        self.deal1 = False
        self.deal2 = False
        self.deal3 = False
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
        self.LP1betMoney = Label(text=str(self.P1betMoney)+"만", width=4, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LP1betMoney.place(x=100, y=500)

        self.LP2betMoney = Label(text=str(self.P2betMoney)+"만", width=4, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LP2betMoney.place(x=300, y=500)

        self.LP3betMoney = Label(text=str(self.P2betMoney)+"만", width=4, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LP3betMoney.place(x=500, y=500)

        self.LplayerMoney = Label(text=str(self.totalMoney)+"만원", width=10, height=1, font=self.fontstyle3, bg="green", fg="blue")
        self.LplayerMoney.place(x=620, y=450)

        # made label
        # self.LplayerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        # self.LplayerMade.place(x=250, y=400)
        #
        # self.LplayerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        # self.LplayerMade.place(x=250, y=400)
        #
        # self.LplayerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        # self.LplayerMade.place(x=250, y=400)
        #
        # self.LdealerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        # self.LdealerMade.place(x=250, y=100)

        # number label
        self.LplayerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMade.place(x=250, y=400)

        self.LplayerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMade.place(x=250, y=400)

        self.LplayerMade = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMade.place(x=250, y=400)

        # win/lose label
        # self.LP1status = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        # self.LP1status.place(x=500, y=350)
        #
        # self.LP2status = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        # self.LP2status.place(x=500, y=350)
        #
        # self.LP3status = Label(text="test", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        # self.LP3status.place(x=500, y=350)

        self.player1.reset()
        self.player2.reset()
        self.player3.reset()
        self.dealer.reset()

        # 카드 덱 40장 셔플링 0,1,,.39
        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        for i in range(5):
            self.hitPlayer1(i)
            self.hitPlayer2(i)
            self.hitPlayer3(i)
            self.hitDealer(i)
        # self.hitPlayer1(1)

    def pressedP1Bet5(self):
        pass

    def pressedP1Bet1(self):
        pass

    def pressedP2Bet5(self):
        pass

    def pressedP2Bet1(self):
        pass

    def pressedP3Bet5(self):
        pass

    def pressedP3Bet1(self):
        pass

    def pressedCheck(self):
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.Deal["state"] = "active"
        self.Deal["bg"] = "white"
        PlaySound('../sounds/chip.wav', SND_FILENAME)

        if self.deckN == 9:
            self.Deal["state"] = "disabled"
            self.Deal["bg"] = "gray"
            self.checkWinner()

    def pressedBx1(self):   # 수정 o
        temp = self.betMoney
        self.betMoney += temp
        if self.playerMoney >= temp:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= temp
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= temp

        if self.deckN == 9:
            self.Deal["state"] = "disabled"
            self.Deal["bg"] = "gray"
            self.checkWinner()

    def pressedBx2(self):    # 수정 o
        temp = self.betMoney * 2
        self.betMoney += temp
        if self.playerMoney >= temp:
            self.LbetMoney.configure(text="$" + str(self.betMoney))
            self.playerMoney -= temp
            self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
            self.Deal["state"] = "active"
            self.Deal["bg"] = "white"
            PlaySound('../sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= temp

        if self.deckN == 9:
            self.Deal["state"] = "disabled"
            self.Deal["bg"] = "gray"
            self.checkWinner()

    def init_deal(self):
        self.player1.reset()
        self.player2.reset()
        self.player3.reset()
        self.dealer.reset()

        # 카드 덱 40장 셔플링 0,1,,.39
        self.cardDeck = [i for i in range(40)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        self.hitPlayer1(0)
        self.hitPlayer2(0)
        self.hitPlayer3(0)
        self.hitDealer(0)

        for i in range(3):
            self.hitMiddle(i)

        self.nCardsPlayer = 1
        self.nCardsDealer = 1
        self.nCardsMiddle = 2

    def hitPlayer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="../cards/" + newCard.filename())
        self.LcardsPlayer.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p

        self.LcardsPlayer[self.player.inHand() - 1].place(x=50 + n * 90, y=350)

        # test 용도
        # self.LplayerMade.configure(text=str(self.player.value()))
        PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer1(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player1.addCard(newCard)
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        self.LcardsPlayer1.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer1[self.player1.inHand() - 1].image = p

        self.LcardsPlayer1[self.player1.inHand() - 1].place(x=50 + n * 30, y=350)

        # test 용도
        # self.LplayerMade.configure(text=str(self.player.value()))
        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer2(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        self.LcardsPlayer2.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer2[self.player2.inHand() - 1].image = p

        self.LcardsPlayer2[self.player2.inHand() - 1].place(x=250 + n * 30, y=350)

        # test 용도
        # self.LplayerMade.configure(text=str(self.player.value()))
        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitPlayer3(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)
        p = PhotoImage(file="../GodoriCards/" + newCard.filename())
        self.LcardsPlayer3.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer3[self.player3.inHand() - 1].image = p

        self.LcardsPlayer3[self.player3.inHand() - 1].place(x=450 + n * 30, y=350)

        # test 용도
        # self.LplayerMade.configure(text=str(self.player.value()))
        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

    def hitDealer(self, n):                 # 수정 o
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="../GodoriCards/cardback.gif")
        self.LcardsDealer.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[self.dealer.inHand() - 1].image = p

        self.LcardsDealer[self.dealer.inHand() - 1].place(x=250 + n * 30, y=100)


        # PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

        # self.Deal['state'] = 'disabled'
        # self.Deal['bg'] = 'gray'

    def pressedDeal(self):      # 수정 o
        if self.deckN == 0:
            self.init_deal()
        else:
            self.nCardsMiddle += 1
            self.hitMiddle(self.nCardsMiddle)
        PlaySound('../sounds/ding.wav', SND_FILENAME)

    def pressedAgain(self):      # 수정 o
        for i in range(2):
            self.LcardsDealer[i].destroy()
            self.LcardsPlayer[i].destroy()

        for i in range(5):
            self.LcardsMiddle[i].destroy()

        self.LcardsDealer.clear()
        self.LcardsPlayer.clear()
        self.LcardsMiddle.clear()

        self.player.reset()
        self.dealer.reset()
        self.middle.reset()
        self.deckN = 0
        self.nCardsDealer = 0
        self.nCardsPlayer = 0
        self.nCardsMiddle = 0
        self.betMoney = 10
        self.playerMoney -= 10
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.Lstatus.configure(text="")
        self.LplayerMade.configure(text="")
        self.LdealerMade.configure(text="")
        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Bx1['state'] = 'active'
        self.Bx1['bg'] = 'white'
        self.Bx2['state'] = 'active'
        self.Bx2['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def checkWinner(self):
        pedigree = {'top': 0, 'one pair': 1, 'two pair': 2, 'triple': 3, 'strait': 4, 'back strait': 5,
                    'mountain': 6, 'flush': 7, 'full house': 8, 'four card': 9, 'strait flush': 10,
                    'back strait flush': 11, 'royal strait flush': 12}

        # 뒤집힌 카드를 다시 그린다.
        for i in range(2):
            p = PhotoImage(file="../cards/" + self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image=p)  # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image = p  # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        self.player.cards += self.middle.cards
        self.dealer.cards += self.middle.cards

        player_ped = self.player.highMade()     # 족보 + top
        dealer_ped = self.dealer.highMade()

        playerhigh = pedigree[player_ped[0]]    # 족보 int
        dealerhigh = pedigree[dealer_ped[0]]    # 족보 int

        # dictionary 만들어서 족보별 우선순위 만들기
        print(playerhigh, dealerhigh)

        if playerhigh == dealerhigh:
            if playerhigh == 8 or playerhigh == 2:  # top 두번 비교
                if player_ped[1] == dealer_ped[1]:
                    if player_ped[2] == dealer_ped[2]:
                        self.push()
                    elif player_ped[2] > dealer_ped[2]:
                        self.win()
                    else:
                        self.lose()
                elif player_ped[1] == 1:
                    self.win()
                elif dealer_ped[1] == 1:
                    self.lose()
                elif player_ped[1] > dealer_ped[1]:
                    self.win()
                else:
                    self.lose()
            else:                                           # top 한번 비교
                if player_ped[1] == dealer_ped[1]:
                    self.push()
                elif player_ped[1] == 1:
                    self.win()
                elif dealer_ped[1] == 1:
                    self.lose()
                elif player_ped[1] > dealer_ped[1]:
                    self.win()
                else:
                    self.lose()
        elif playerhigh > dealerhigh:
            self.win()
        elif playerhigh < dealerhigh:
            self.lose()

        if playerhigh == 11 or playerhigh == 12 or playerhigh == 5 or playerhigh == 6:
            self.LplayerMade.configure(text=player_ped[0])
        else:
            temp = ' '
            if player_ped[1] == 11:
                temp = 'J '
                self.LplayerMade.configure(text=temp+player_ped[0])
            elif player_ped[1] == 12:
                temp = 'Q '
                self.LplayerMade.configure(text=temp+player_ped[0])
            elif player_ped[1] == 13:
                temp = 'K '
                self.LplayerMade.configure(text=temp+player_ped[0])
            elif player_ped[1] == 1:
                temp = 'Ace '
                self.LplayerMade.configure(text=temp+player_ped[0])
            else:
                self.LplayerMade.configure(text=str(player_ped[1])+temp+player_ped[0])

        if dealerhigh == 11 or dealerhigh == 12 or dealerhigh == 5 or dealerhigh == 6:
            self.LdealerMade.configure(text=dealer_ped[0])
        else:
            temp = ' '
            if dealer_ped[1] == 11:
                temp = 'J '
                self.LdealerMade.configure(text=temp+dealer_ped[0])
            elif dealer_ped[1] == 12:
                temp = 'Q '
                self.LdealerMade.configure(text=temp+dealer_ped[0])
            elif dealer_ped[1] == 13:
                temp = 'K '
                self.LdealerMade.configure(text=temp+dealer_ped[0])
            elif dealer_ped[1] == 1:
                temp = 'Ace '
                self.LdealerMade.configure(text=temp+dealer_ped[0])
            else:
                self.LdealerMade.configure(text=str(dealer_ped[1])+temp+dealer_ped[0])

        self.betMoney = 0
        self.LplayerMoney.configure(text="You have $" + str(self.playerMoney))
        self.LbetMoney.configure(text="$" + str(self.betMoney))
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Bx1['state'] = 'disabled'
        self.Bx1['bg'] = 'gray'
        self.Bx2['state'] = 'disabled'
        self.Bx2['bg'] = 'gray'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

    def win(self):
        self.playerMoney += self.betMoney * 2
        self.Lstatus.configure(text="Win")
        PlaySound('../sounds/win.wav', SND_FILENAME)

    def lose(self):
        self.Lstatus.configure(text="Lose")
        PlaySound('../sounds/wrong.wav', SND_FILENAME)

    def push(self):
        self.playerMoney += self.betMoney
        self.Lstatus.configure(text="Push")
        PlaySound('../sounds/win.wav', SND_FILENAME)

Dori()
