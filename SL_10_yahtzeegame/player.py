class Player:
    UPPER = 6  # upper category 6개
    LOWER = 7  # lower category 7개

    def __init__(self, name):
        self.name = name
        self.scores = [0 for _ in range(self.UPPER + self.LOWER)]       # 13개 category점수
        self.used = [False for _ in range(self.UPPER + self.LOWER)]     # 13개 category 사용여부

    def setScore(self, score, index):       # 인자로 index를 받아서 해당 카테고리 점수 기입
        self.scores[index] = score

    def setAtUsed(self, index):     # 인자로 index를 받아서 해당 카테고리는 사용으로 설정
        self.used[index] = True

    def getUpperScore(self):        # 상위 6개 점수 합을 반환
        s = 0
        for i in range(self.UPPER):
            s += self.scores[i]
        self.upperScore = s
        return self.upperScore

    def getLowerScore(self):    #
        s = 0
        for i in range(self.LOWER):
            s += self.scores[self.UPPER + i]
        self.lowerScore = s
        return self.lowerScore

    def getUsed(self):
        return self.used

    def getTotalScore(self):
        total = 0
        for i in range(len(self.scores)):
            total += self.scores[i]
        return total

    def toString(self):
        return self.name

    def allLowerUsed(self):     # lower category 7개 모두 사용되었는가 ?
        for i in range(self.LOWER):
            if self.used[i] == False:
                return False
        return True

    # upper category 6개 모두 사용되었는가 ?
    # UpperScores, UpperBonus 계산에 활용
    def allUpperUsed(self):
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True
