from dice import *

class Configuration:
    configs = ["Category", "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
                "Upper Scores", "Upper Bonus(35)", "Three of a kind", "Four of a kind", "Full House(25)",
                "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance", "Lower Scores", "Total"]

    @staticmethod
    def getConfigs():   # 정적 메소드: 객체생성 없이 사용 가능
        return Configuration.configs

    @staticmethod
    # 정적 메소드: 객체생성 없이 사용 가능
    # row에 따라 주사위 점수를 계산 반환. 예를 들어, row가 0이면 "Ones"가 채점되어야 함을
    # 의미합니다. row가 2이면, "Threes"가 득점되어야 함을 의미합니다. row가 득점 (scored)하지
    # 않아야 하는 버튼 (즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우
    # -1을 반환합니다.
    def score(row, d):
        if 0 <= row <= 6:
            return Configuration.scoreUpper(d, row+1)
        elif row == 8:
            return Configuration.scoreThreeOfAKind(d)
        elif row == 9:
            return Configuration.scoreFourOfAKind(d)
        elif row == 10:
            return Configuration.scoreFullHouse(d)
        elif row == 11:
            return Configuration.scoreSmallStraight(d)
        elif row == 12:
            return Configuration.scoreLargeStraight(d)
        elif row == 13:
            return Configuration.scoreYahtzee(d)
        elif row == 14:
            return Configuration.sumDie(d)
        else:
            return -1


    @staticmethod
    # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
    # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.
    def scoreUpper(d, num):
        s = 0
        for i in range(5):
            if d[i].getRoll() == num:
                s += num
        return s

    @staticmethod
    def scoreThreeOfAKind(d):   # 조건을 만족하면 sumDice 반환
        count = [0 for _ in range(6)]
        for i in range(5):
            count[d[i].getRoll() - 1] += 1
        if (3 or 4 or 5) in count:
            return Configuration.sumDie(d)
        return 0

    @staticmethod
    def scoreFourOfAKind(d):    # 조건을 만족하면 sumDice 반환
        count = [0 for _ in range(6)]
        for i in range(5):
            count[d[i].getRoll() - 1] += 1
        if (4 or 5) in count:
            return Configuration.sumDie(d)
        return 0

    @staticmethod
    def scoreFullHouse(d):  # 25
        count = [0 for _ in range(6)]
        for i in range(5):
            count[d[i].getRoll() - 1] += 1
        if (3 and 2) in count:
            return 25
        return 0

    @staticmethod
    # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
    # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5
    def scoreSmallStraight(d):  # 30
        count = [0 for _ in range(6)]
        for i in range(5):
            count[d[i].getRoll() - 1] += 1
        for i in range(3):
            flag = 0
            for j in range(4):
                if count[i+j] == 0:
                    break
                else:
                    flag += 1
            if flag == 4:
                return 30
        return 0

    @staticmethod
    def scoreLargeStraight(d):       # 1 2 3 4 5 혹은 2 3 4 5 6 검사(40)
        count = [0 for _ in range(6)]
        for i in range(5):
            count[d[i].getRoll() - 1] += 1

        for i in range(2):
            flag = 0
            for j in range(5):
                if count[i + j] == 0:
                    break
                else:
                    flag += 1
            if flag == 5:
                return 40
        return 0

    @staticmethod
    def scoreYahtzee(d):    # 50
        count = [0 for _ in range(6)]
        for i in range(5):
            count[d[i].getRoll() - 1] += 1

        if 5 in count:
            return 50
        return 0

    @staticmethod
    def sumDie(d):         # 주사위들의 합 리턴
        s = 0
        for i in range(5):
            s += d[i].getRoll()
        return s
