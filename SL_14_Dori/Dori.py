from tkinter import *
from tkinter import font
from winsound import *
from Dori_player import *
from Dori_card import *
import random


class BlackJack:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem Poker")
        self.window.geometry("800x600")
        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()
        self.player = Player("player")
        self.dealer = Player("dealer")
        self.middle = Player("middle")
        self.betMoney = 10
        self.playerMoney = 990
        self.nCardsDealer = 0
        self.nCardsPlayer = 0
        self.nCardsMiddle = 0
        self.LcardsPlayer = []
        self.LcardsDealer = []
        self.LcardsMiddle = []
        self.deckN = 0
        self.window.mainloop()

    def setupButton(self):
        self.Check = Button(self.window, text="Check", width=6, height=1, font=self.fontstyle2, command=self.pressedCheck)
        self.Check.place(x=50, y=500)
        self.Bx1 = Button(self.window, text="Bet x1", width=6, height=1, font=self.fontstyle2, command=self.pressedBx1)
        self.Bx1.place(x=150, y=500)
        self.Bx2 = Button(self.window, text="Bet x2", width=6, height=1, font=self.fontstyle2, command=self.pressedBx2)
        self.Bx2.place(x=250, y=500)
        self.Deal = Button(self.window, text="Deal", width=6, height=1, font=self.fontstyle2, command=self.pressedDeal)
        self.Deal.place(x=600, y=500)
        self.Again = Button(self.window, text="Again", width=6, height=1, font=self.fontstyle2, command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    # text 위치 수정
    def setupLabel(self):
        self.LbetMoney = Label(text="$10", width=4, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LbetMoney.place(x=200, y=450)
        self.LplayerMoney = Label(text="You have $990", width=15, height=1, font=self.fontstyle, bg="green", fg="yellow")
        self.LplayerMoney.place(x=500, y=450)
        self.LplayerMade = Label(text="", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LplayerMade.place(x=250, y=400)
        self.LdealerMade = Label(text="", width=12, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LdealerMade.place(x=250, y=100)
        self.Lstatus = Label(text="", width=12, height=1, font=self.fontstyle, bg="green", fg="red")
        self.Lstatus.place(x=500, y=350)

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
        self.player.reset()
        self.dealer.reset()
        self.middle.reset()

        # 카드 덱 52장 셔플링 0,1,,.51
        self.cardDeck = [i for i in range(52)]
        random.shuffle(self.cardDeck)
        self.deckN = 0

        for i in range(2):
            self.hitPlayer(i)
            self.hitDealer(i)

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

    def hitDealer(self, n):                 # 수정 o
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="../cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsDealer[self.dealer.inHand() - 1].image = p

        self.LcardsDealer[self.dealer.inHand() - 1].place(x=50 + n * 90, y=50)

        # test 용도
        # self.LdealerMade.configure(text=str(self.dealer.value()))

        PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

    def hitMiddle(self, n):
        newCard = Card(self.cardDeck[self.deckN])

        self.deckN += 1
        self.middle.addCard(newCard)
        p = PhotoImage(file="../cards/" + newCard.filename())
        self.LcardsMiddle.append(Label(self.window, image=p))

        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsMiddle[self.middle.inHand() - 1].image = p

        self.LcardsMiddle[self.middle.inHand() - 1].place(x=150 + n * 90, y=200)

        PlaySound('../sounds/cardFlip1.wav', SND_FILENAME)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'

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

BlackJack()