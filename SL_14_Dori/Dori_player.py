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
        made = False
        result = []
        index = []
        temp = []
        for i in range(self.N):
            temp.append(self.cards[i].getMonth())
        print(temp)

        # 메이드 족보
        # 콩콩팔 (1 1 8) 삐리칠 (1 2 7) 물삼육 (1 3 6) 빽새오 (1 4 5) 삥구장 (1 9 10)
        # 니니육 (2 2 6) 이삼오 (2 3 5) 이판장 (2 8 10)
        # 심심새 (3 3 4) 삼칠장 (3 7 10) 삼빡구 (3 8 9)
        # 살살이 (4 4 2) 사륙장 (4 6 10) 사칠구 (4 7 9)
        # 꼬꼬장 (5 5 10) 오륙구 (5 6 9) 오리발 (5 7 8)
        # 쭉쭉팔 (6 6 8)
        # 철철육 (7 7 6)
        # 팍팍싸 (8 8 4)
        # 구구리 (9 9 2)
        # 장장장 (10 10 10)


        if temp.count(1) >= 2 and 8 in temp:
            result.append('콩콩팔 (1 1 8)')
            index.append(list(filter(lambda x: temp[x] == 2 or temp[x] == 8, range(len(temp)))))
        if 1 in temp and 2 in temp and 7 in temp:
            result.append('삐리칠 (1 2 7)')
            index.append(list(filter(lambda x: temp[x] == 1 or temp[x] == 2 or temp[x] == 7, range(len(temp)))))
        if 1 in temp and 3 in temp and 6 in temp:
            result.append('물삼육 (1 3 6)')
            index.append(list(filter(lambda x: temp[x] == 1 or temp[x] == 3 or temp[x] == 6, range(len(temp)))))
        if 1 in temp and 4 in temp and 5 in temp:
            result.append('빽새오 (1 4 5)')
            index.append(list(filter(lambda x: temp[x] == 1 or temp[x] == 4 or temp[x] == 5, range(len(temp)))))
        if 1 in temp and 9 in temp and 10 in temp:
            result.append('삥구장 (1 9 10)')
            index.append(list(filter(lambda x: temp[x] == 1 or temp[x] == 9 or temp[x] == 10, range(len(temp)))))
        if temp.count(2) >= 2 and 6 in temp:
            result.append('니니육 (2 2 6)')
            index.append(list(filter(lambda x: temp[x] == 2 or temp[x] == 6, range(len(temp)))))
        if 2 in temp and 3 in temp and 5 in temp:
            result.append('이삼오 (2 3 5)')
            index.append(list(filter(lambda x: temp[x] == 2 or temp[x] == 3 or temp[x] == 5, range(len(temp)))))
        if 2 in temp and 8 in temp and 10 in temp:
            result.append('이판장 (2 8 10)')
            index.append(list(filter(lambda x: temp[x] == 2 or temp[x] == 8 or temp[x] == 10, range(len(temp)))))
        if temp.count(3) >= 2 and 4 in temp:
            result.append('심심새 (3 3 4)')
            index.append(list(filter(lambda x: temp[x] == 3 or temp[x] == 4, range(len(temp)))))
        if 3 in temp and 7 in temp and 10 in temp:
            result.append('삼칠장 (3 7 10)')
            index.append(list(filter(lambda x: temp[x] == 3 or temp[x] == 7 or temp[x] == 10, range(len(temp)))))
        if 3 in temp and 8 in temp and 9 in temp:
            result.append('삼빡구 (3 8 9)')
            index.append(list(filter(lambda x: temp[x] == 3 or temp[x] == 8 or temp[x] == 9, range(len(temp)))))
        if temp.count(4) >= 2 and 2 in temp:
            result.append('살살이 (4 4 2)')
            index.append(list(filter(lambda x: temp[x] == 4 or temp[x] == 2, range(len(temp)))))
        if 4 in temp and 6 in temp and 10 in temp:
            result.append('사륙장 (4 6 10)')
            index.append(list(filter(lambda x: temp[x] == 4 or temp[x] == 6 or temp[x] == 10, range(len(temp)))))
        if 4 in temp and 7 in temp and 9 in temp:
            result.append('사칠구 (4 7 9)')
            index.append(list(filter(lambda x: temp[x] == 4 or temp[x] == 7 or temp[x] == 9, range(len(temp)))))
        if temp.count(5) >= 2 and 10 in temp:
            result.append('꼬꼬장 (5 5 10)')
            index.append(list(filter(lambda x: temp[x] == 5 or temp[x] == 10, range(len(temp)))))
        if 5 in temp and 6 in temp and 9 in temp:
            result.append('오륙구 (5 6 9)')
            index.append(list(filter(lambda x: temp[x] == 5 or temp[x] == 6 or temp[x] == 9, range(len(temp)))))
        if 5 in temp and 7 in temp and 8 in temp:
            result.append('오리발 (5 7 8)')
            index.append(list(filter(lambda x: temp[x] == 5 or temp[x] == 7 or temp[x] == 8, range(len(temp)))))
        if temp.count(6) >= 2 and 8 in temp:
            result.append('쭉쭉팔 (6 6 8)')
            index.append(list(filter(lambda x: temp[x] == 6 or temp[x] == 8, range(len(temp)))))
        if temp.count(7) >= 2 and 6 in temp:
            result.append('철철육 (7 7 6)')
            index.append(list(filter(lambda x: temp[x] == 7 or temp[x] == 6, range(len(temp)))))
        if temp.count(8) >= 2 and 4 in temp:
            result.append('팍팍싸 (8 8 4)')
            index.append(list(filter(lambda x: temp[x] == 8 or temp[x] == 4, range(len(temp)))))
        if temp.count(9) >= 2 and 2 in temp:
            result.append('구구리 (9 9 2)')
            index.append(list(filter(lambda x: temp[x] == 9 or temp[x] == 2, range(len(temp)))))
        if temp.count(10) >= 3:
            result.append('장장장 (10 10 10)')
            index.append(list(filter(lambda x: temp[x] == 10, range(len(temp)))))

        print(result)
        print(index)


        # 짜투리 족보
        # 1~9끗
        # 망통(0끗)
        # 광땡(13 18 38)
        # 1~9땡 + 장땡

