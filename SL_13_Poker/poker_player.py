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

    def highMade(self):  # 미완성

        pattern = dict()
        number = dict()

        for i in range(4):
            pattern[i] = []

        for i in range(1, 13 + 1):
            number[i] = []

        for i in range(len(self.cards)):
            pattern[self.cards[i].x].append(self.cards[i].value)
            number[self.cards[i].value].append(self.cards[i].x)

        ped_result = [self.royal_strait_flush(pattern), self.back_strait_flush(pattern), self.strait_flush(pattern),
                      self.four_card(number), self.full_house(number), self.flush(pattern), self.mountain(number),
                      self.back_strait(number), self.strait(number), self.triple(number), self.two_pair(number),
                      self.one_pair(number)
                      ]

        if ped_result[0]:    # push
            return ['royal strait flush', -1]
        elif ped_result[1]:   # push
            return ['back strait flush', -1]
        elif ped_result[2][0]:
            return ['strait flush', ped_result[2][1]]
        elif ped_result[3][0]:
            return ['four card', ped_result[3][1]]
        elif ped_result[4][0]:
            return ['full house', ped_result[4][1], ped_result[4][2]]
        elif ped_result[5][0]:
            return ['flush', ped_result[5][1]]
        elif ped_result[6]:
            return ['mountain', -1]
        elif ped_result[7]:
            return ['back strait', -1]
        elif ped_result[8][0]:
            return ['strait', ped_result[8][1]]
        elif ped_result[9][0]:
            return ['triple', ped_result[9][1]]
        elif ped_result[10][0]:
            return ['two pair', ped_result[10][1], ped_result[10][2]]
        elif ped_result[11][0]:
            return ['one pair', ped_result[11][1]]
        else:
            if len(number[1]) == 1:
                return ['top', 1]
            else:
                for i in range(13, 1, -1):
                    if len(number[i]) == 1:
                        return ['top', i]

    def royal_strait_flush(self, p):
        for i in range(4):
            if (10, 11, 12, 13, 1) in p[i]:
                return True
        return False

    def back_strait_flush(self, p):
        for i in range(4):
            if (1, 2, 3, 4, 5) in p[i]:
                return True
        return False

    def strait_flush(self, p):
        result = []
        flag = []
        for i in range(4):
            if len(p[i]) >= 5:
                temp = sorted(p[i])
                for j in range(len(temp) - 4):
                    if temp[j] == temp[j + 4] - 4:
                        flag.append(temp[j+4])

        if len(flag) == 0:
            result = [False]
            return result
        else:
            m = max(flag)
            if m == 5:
                result = [True, 1]
            else:
                result = [True, m]
            return result

    def four_card(self, n):
        for i in range(1, 13 + 1):
            if len(n[i]) == 4:
                return [True, i]
        return [False]

    def full_house(self, n):
        three = []
        two = []
        for i in range(1, 13 + 1):
            if len(n[i]) == 3:
                three.append(i)
            if len(n[i]) == 2:
                two.append(i)

        if len(three) == 2:
            temp = sorted(three)
            if temp[0] == 1:
                return [True, temp[0], temp[1]]
            else:
                return [True, temp[1], temp[0]]
        elif len(three) == 1 and len(two) == 1:
            return [True, three[0], two[0]]
        elif len(three) == 1 and len(two) == 2:
            temp = sorted(two)
            if temp[0] == 1:
                return [True, three[0], temp[0]]
            else:
                return [True, three[0], temp[1]]
        else:
            return [False]

    def flush(self, p):
        for i in range(4):
            if len(p[i]) >= 5:
                t = sorted(p[i])
                if t[0] == 1:
                    return [True, t[0]]
                else:
                    return [True, max(t)]
        return [False]

    def mountain(self, n):
        for i in range(10, 13 + 1):
            if len(n[i]) == 0:
                return False

        if len(n[1]) == 0:
            return False

        return True

    def back_strait(self, n):
        for i in range(1, 5 + 1):
            if len(n[i]) == 0:
                return False
        return True

    def strait(self, n):
        result = []
        for i in range(1, 9 + 1):
            flag = True
            for j in range(i, i + 5):
                if len(n[j]) == 0:
                    flag = False
            if flag:
                result.append(i+4)

        if len(result) == 0:
            return [False]
        else:
            m = max(result)
            if m == 5:
                return [True, 1]
            else:
                return [True, m]

    def triple(self, n):
        result = []
        for i in range(1, 13 + 1):
            if len(n[i]) == 3:
                result.append(i)

        if len(result) == 0:
            return [False]
        else:
            m = sorted(result)
            if m[0] == 1:
                return [True, 1]
            else:
                return [True, m[-1]]

    def two_pair(self, n):
        count = []
        for i in range(1, 13 + 1):
            if len(n[i]) == 2:
                count.append(i)

        if len(count) >= 2:
            t = sorted(count)   # 1일때 수정
            if t[0] == 1:
                return [True, t[0], t[-1]]
            else:
                return [True, t[-1], t[-2]]
        else:
            return [False]

    def one_pair(self, n):
        for i in range(1, 13 + 1):
            if len(n[i]) == 2:
                return [True, i]
        return [False]
