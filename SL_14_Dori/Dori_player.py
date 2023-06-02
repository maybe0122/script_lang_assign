class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0

    def inHand(self):
        return self.N

    def addCard(self, c):
        self.cards.append(c)
        self.N += 1

    def reset(self):
        self.N = 0
        self.cards.clear()

    def made(self):  # 미완성
        result = []
        temp = []
        for i in range(self.N):
            temp.append(self.cards[i].getinfo())
        print(temp)

        # 콩콩팔 (1 1 8)
        # 삐리칠 (1 2 7)
        # 물삼육 (1 3 6)
        # 빽새오 (1 4 5)
        # 삥구장 (1 9 10)
        # 니니육 (2 2 6)
        # 이삼오 (2 3 4)
        # 이판장 (2 8 10)
        # 심심새 (3 3 4)
        # 삼칠장 (3 7 10)
        # 삼빡구 (3 8 9)
        # 살살이 (4 4 2)
        # 사륙장 (4 6 10)
        # 사칠구 (4 7 9)
        # 꼬꼬장 (5 5 10)
        # 오륙구 (5 6 9)
        # 오리발 (5 7 8)
        # 쭉쭉팔 (6 6 8)
        # 철철육 (7 7 6)
        # 팍팍싸 (8 8 4)
        # 구구리 (9 9 2)
        # 장장장 (10 10 10)

