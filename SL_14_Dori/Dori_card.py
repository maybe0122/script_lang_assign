class Card:     # 클래스 Card
    def __init__(self, number):         # 랜덤 넘버 number = 0..39 값 인자로 전달
        self.month = number // 4 + 1          # 1,...,10 -> 월
        self.num = number % 4 + 1    # 1, 2, 3, 4 (한 월에 있는 4가지 무늬의 같은 카드를 숫자로 구분)
        self.info = [self.month, self.num]

    def filename(self):         # 랜덤 넘버 number =0..39 에서 file name 반환
        return str(self.month)+"."+str(self.num)+'.gif'

    def getMonth(self):         # 1,2,3,4,5,6,7,8,9,10 월
        return self.month

    def getinfo(self):
        return self.info

    def getNum(self):
        return self.num
