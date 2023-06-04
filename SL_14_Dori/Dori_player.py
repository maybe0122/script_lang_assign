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

    def check(self, card):
        month = [card[0].getMonth(), card[1].getMonth()]
        num = [card[0].getNum(), card[1].getNum()]
        # print(month, num)

        if month[0] == month[1]:
            if month[0] == 10:
                return '장땡'
            return str(month[0])+'땡'
        else:
            if 1 in month and 3 in month and sum(num) == 2:
                return '13광땡'
            elif 1 in month and 8 in month and sum(num) == 2:
                return '18광땡'
            elif 3 in month and 8 in month and sum(num) == 2:
                return '38광땡'
            else:
                if sum(month) % 10 == 0:
                    return '망통'
                else:
                    return str(sum(month) % 10)+'끗'

    def made(self):  # 미완성
        pedigree = ['망통', '1끗', '2끗', '3끗', '4끗', '5끗', '6끗', '7끗', '8끗', '9끗', '1땡', '2땡', '3땡', '4땡', '5땡',
                    '6땡', '7땡', '8땡', '9땡', '장땡', '13광땡', '18광땡', '38광땡']
        made = False
        result = []
        index = []
        rest = []
        temp = []
        made_index = []

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
            one = list(filter(lambda x: temp[x] == 1, range(len(temp))))

            index = list(filter(lambda x: temp[x] == 1 or temp[x] == 8, range(len(temp))))
            if len(index) == 3:
                idx = []
                for i in range(5):
                    if i not in index:
                        idx.append(self.cards[i])
                rest.append(self.check(idx))
                made_index.append(index)
            elif len(index) == 4:
                check_list = []     # 족보 판별을 위한 list
                idx = []            # made 인덱스
                if len(one) == 3:   # 1 1 1 8
                    cnt = 0         # 1개수
                    for i in range(5):
                        if temp[i] == 1 and self.cards[i].getNum() == 1:      # 1광이면 패스
                            pass
                        elif temp[i] == 8:                                  # 8이면 메이드 인덱스에 추가
                            idx.append(i)
                        else:
                            if cnt >= 2:                                    # 1의 개수가 2개일 때까지 메이드 인덱스에 추가
                                break
                            else:
                                idx.append(i)
                                cnt += 1

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                    made_index.append(idx)
                elif len(one) == 2:     # 1 1 8 8
                    cnt = 0  # 8개수
                    for i in range(5):
                        if temp[i] == 8 and self.cards[i].getNum() == 1:  # 8광이면 패스
                            pass
                        elif temp[i] == 1:  # 1이면 메이드 인덱스에 추가
                            idx.append(i)
                        else:
                            if cnt >= 1:  # 8의 개수가 1개일 때까지 메이드 인덱스에 추가
                                continue
                            else:
                                idx.append(i)
                                cnt += 1

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                    made_index.append(idx)
            elif len(index) == 5:
                idx = []
                if len(one) == 4:       # 1 1 1 1 8
                    cnt = 0     # 1개수
                    for i in range(5):
                        if temp[i] == 1:
                            if cnt >= 2:
                                continue
                            else:
                                idx.append(i)
                                cnt += 1
                        else:
                            idx.append(i)
                    made_index.append(idx)
                    rest.append('1땡')
                elif len(one) == 3:     # 1 1 1 8 8
                    o = -1
                    e = -1
                    for i in range(5):
                        if self.cards[i].getMonth() == 1 and self.cards[i].getNum() == 1:
                            o = i
                        elif self.cards[i].getMonth() == 8 and self.cards[i].getNum() == 1:
                            e = i

                    if o != -1 and e != -1:
                        rest.append('18광땡')
                        for i in range(5):
                            if i == o or i == e:
                                pass
                            else:
                                idx.append(i)
                        made_index.append(idx)
                    else:
                        one_cnt = 0
                        eight_count = 0
                        rest.append('9끗')
                        for i in range(5):
                            if temp[i] == 1 and one_cnt != 2:
                                idx.append(i)
                                one_cnt += 1
                            elif temp[i] == 8 and eight_count != 1:
                                idx.append(i)
                                eight_count += 1
                elif len(one) == 2:     # 1 1 8 8 8
                    cnt = 0  # 1개수
                    for i in range(5):
                        if temp[i] == 8:
                            if cnt >= 1:
                                continue
                            else:
                                idx.append(i)
                                cnt += 1
                        else:
                            idx.append(i)
                    made_index.append(idx)
                    rest.append('8땡')
            made = True

        if 1 in temp and 2 in temp and 7 in temp:
            result.append('삐리칠 (1 2 7)')
            index = list(filter(lambda x: temp[x] == 1 or temp[x] == 2 or temp[x] == 7, range(len(temp))))
            one = list(filter(lambda x: temp[x] == 1, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(one) == 1:
                n1 = 0
                n2 = 0
                n7 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 2 and n2 != 1:
                        idx.append(i)
                        n2 += 1
                    elif temp[i] == 7 and n7 != 1:
                        idx.append(i)
                        n7 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 1 and self.cards[i].getNum() == 1:
                        o = i

                n1 = 0
                n2 = 0
                n7 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1 and i != o:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 2 and n2 != 1:
                        idx.append(i)
                        n2 += 1
                    elif temp[i] == 7 and n7 != 1:
                        idx.append(i)
                        n7 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if 1 in temp and 3 in temp and 6 in temp:
            result.append('물삼육 (1 3 6)')
            index = list(filter(lambda x: temp[x] == 1 or temp[x] == 3 or temp[x] == 6, range(len(temp))))
            one = (list(filter(lambda x: temp[x] == 1, range(len(temp)))))
            three = (list(filter(lambda x: temp[x] == 3, range(len(temp)))))

            if len(one) == 1 and len(three) == 1:
                idx = []
                check_list = []
                n1 = 0
                n3 = 0
                n6 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 3 and n3 != 1:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 6 and n6 != 1:
                        idx.append(i)
                        n6 += 1
                made_index.append(idx)
                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])
                rest.append(self.check(check_list))
            elif len(one) >= 2 and len(three) == 1:
                idx = []
                check_list = []
                n1 = 0
                n3 = 0
                n6 = 0
                o = -1

                for i in range(5):
                    if self.cards[i].getMonth() == 1 and self.cards[i].getNum() == 1:
                        o = i

                if o != -1:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1 and i != o:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                else:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))

            elif len(three) >= 2 and len(one) == 1:
                idx = []
                check_list = []
                n1 = 0
                n3 = 0
                n6 = 0
                o = -1

                for i in range(5):
                    if self.cards[i].getMonth() == 3 and self.cards[i].getNum() == 1:
                        o = i

                if o != -1:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1 and i != o:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                else:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
            elif len(three) == 2 and len(one) == 2:
                idx = []
                check_list = []
                n1 = 0
                n3 = 0
                n6 = 0
                o = -1
                t = -1

                for i in range(5):
                    if self.cards[i].getMonth() == 1 and self.cards[i].getNum() == 1:
                        o = i
                    elif self.cards[i].getMonth() == 3 and self.cards[i].getNum() == 1:
                        t = i

                if o != -1 and t != -1:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1 and i != o:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1 and i != t:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                elif o != -1 and t == -1:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1 and i != o:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                elif o == -1 and t != -1:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1  and i != t:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                else:
                    for i in range(5):
                        if temp[i] == 1 and n1 != 1:
                            idx.append(i)
                            n1 += 1
                        elif temp[i] == 3 and n3 != 1:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 6 and n6 != 1:
                            idx.append(i)
                            n6 += 1
                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))

            made = True

        if 1 in temp and 4 in temp and 5 in temp:
            result.append('빽새오 (1 4 5)')
            index = (list(filter(lambda x: temp[x] == 1 or temp[x] == 4 or temp[x] == 5, range(len(temp)))))

            one = list(filter(lambda x: temp[x] == 1, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(one) == 1:
                n1 = 0
                n4 = 0
                n5 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 4 and n4 != 1:
                        idx.append(i)
                        n4 += 1
                    elif temp[i] == 5 and n5 != 1:
                        idx.append(i)
                        n5 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 1 and self.cards[i].getNum() == 1:
                        o = i

                n1 = 0
                n4 = 0
                n5 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1 and i != o:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 4 and n4 != 1:
                        idx.append(i)
                        n4 += 1
                    elif temp[i] == 5 and n5 != 1:
                        n5 += 1
                        idx.append(i)

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if 1 in temp and 9 in temp and 10 in temp:
            result.append('삥구장 (1 9 10)')
            index = (list(filter(lambda x: temp[x] == 1 or temp[x] == 9 or temp[x] == 10, range(len(temp)))))

            one = list(filter(lambda x: temp[x] == 1, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(one) == 1:
                n1 = 0
                n9 = 0
                n10 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 9 and n9 != 1:
                        idx.append(i)
                        n9 += 1
                    elif temp[i] == 10 and n10 != 1:
                        idx.append(i)
                        n10 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 1 and self.cards[i].getNum() == 1:
                        o = i

                n1 = 0
                n9 = 0
                n10 = 0
                for i in range(5):
                    if temp[i] == 1 and n1 != 1 and i != o:
                        idx.append(i)
                        n1 += 1
                    elif temp[i] == 9 and n9 != 1:
                        idx.append(i)
                        n9 += 1
                    elif temp[i] == 10 and n10 != 1:
                        idx.append(i)
                        n10 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if temp.count(2) >= 2 and 6 in temp:
            result.append('니니육 (2 2 6)')
            index = (list(filter(lambda x: temp[x] == 2 or temp[x] == 6, range(len(temp)))))

            idx = []
            check_list = []

            n2 = 0
            n6 = 0
            for i in range(5):
                if temp[i] == 2 and n2 != 2:
                    idx.append(i)
                    n2 += 1
                elif temp[i] == 6 and n6 != 1:
                    idx.append(i)
                    n6 += 1

            made_index.append(idx)
            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            rest.append(self.check(check_list))

            made = True

        if 2 in temp and 3 in temp and 5 in temp:
            result.append('이삼오 (2 3 5)')
            index = (list(filter(lambda x: temp[x] == 2 or temp[x] == 3 or temp[x] == 5, range(len(temp)))))

            three = list(filter(lambda x: temp[x] == 3, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(three) == 1:
                n2 = 0
                n3 = 0
                n5 = 0
                for i in range(5):
                    if temp[i] == 2 and n2 != 1:
                        idx.append(i)
                        n2 += 1
                    elif temp[i] == 3 and n3 != 1:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 5 and n5 != 1:
                        idx.append(i)
                        n5 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 3 and self.cards[i].getNum() == 1:
                        o = i

                n2 = 0
                n3 = 0
                n5 = 0
                for i in range(5):
                    if temp[i] == 3 and n3 != 1 and i != o:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 2 and n2 != 1:
                        idx.append(i)
                        n2 += 1
                    elif temp[i] == 5 and n5 != 1:
                        idx.append(i)
                        n5 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if 2 in temp and 8 in temp and 10 in temp:
            result.append('이판장 (2 8 10)')
            index = (list(filter(lambda x: temp[x] == 2 or temp[x] == 8 or temp[x] == 10, range(len(temp)))))

            eight = list(filter(lambda x: temp[x] == 1, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(eight) == 1:
                n2 = 0
                n8 = 0
                n10 = 0
                for i in range(5):
                    if temp[i] == 2 and n2 != 1:
                        idx.append(i)
                        n2 += 1
                    elif temp[i] == 8 and n8 != 1:
                        idx.append(i)
                        n8 += 1
                    elif temp[i] == 10 and n10 != 1:
                        idx.append(i)
                        n10 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 8 and self.cards[i].getNum() == 1:
                        o = i

                n2 = 0
                n8 = 0
                n10 = 0
                for i in range(5):
                    if temp[i] == 8 and n8 != 1 and i != o:
                        idx.append(i)
                        n8 += 1
                    elif temp[i] == 2 and n2 != 1:
                        idx.append(i)
                        n2 += 1
                    elif temp[i] == 10 and n10 != 1:
                        idx.append(i)
                        n10 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if temp.count(3) >= 2 and 4 in temp:
            result.append('심심새 (3 3 4)')
            index = (list(filter(lambda x: temp[x] == 3 or temp[x] == 4, range(len(temp)))))
            three = (list(filter(lambda x: temp[x] == 3, range(len(temp)))))

            if len(three) == 2:
                idx = []
                check_list = []
                n3 = 0
                n4 = 0

                for i in range(5):
                    if temp[i] == 3 and n3 != 2:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 4 and n4 != 1:
                        idx.append(i)
                        n4 += 1

                made_index.append(idx)

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                rest.append(self.check(check_list))
            else:
                idx = []
                check_list = []
                n3 = 0
                n4 = 0
                t = -1

                for i in range(5):
                    if temp[i] == 3 and self.cards[i].getNum() == 1:
                        t = i

                if t != -1:
                    for i in range(5):
                        if temp[i] == 3 and n3 != 2 and t != i:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 4 and n4 != 1:
                            idx.append(i)
                            n4 += 1

                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                else:
                    for i in range(5):
                        if temp[i] == 3 and n3 != 2:
                            idx.append(i)
                            n3 += 1
                        elif temp[i] == 4 and n4 != 1:
                            idx.append(i)
                            n4 += 1

                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))

            made = True

        if 3 in temp and 7 in temp and 10 in temp:
            result.append('삼칠장 (3 7 10)')
            index = (list(filter(lambda x: temp[x] == 3 or temp[x] == 7 or temp[x] == 10, range(len(temp)))))

            three = list(filter(lambda x: temp[x] == 3, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(three) == 1:
                n3 = 0
                n7 = 0
                n10 = 0
                for i in range(5):
                    if temp[i] == 3 and n3 != 1:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 7 and n7 != 1:
                        idx.append(i)
                        n7 += 1
                    elif temp[i] == 10 and n10 != 1:
                        idx.append(i)
                        n10 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 3 and self.cards[i].getNum() == 1:
                        o = i

                n3 = 0
                n7 = 0
                n10 = 0
                for i in range(5):
                    if temp[i] == 3 and n3 != 1 and i != o:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 7 and n7 != 1:
                        idx.append(i)
                        n7 += 1
                    elif temp[i] == 10 and n10 != 1:
                        idx.append(i)
                        n10 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if 3 in temp and 8 in temp and 9 in temp:
            result.append('삼빡구 (3 8 9)')
            index = (list(filter(lambda x: temp[x] == 3 or temp[x] == 8 or temp[x] == 9, range(len(temp)))))

            three = list(filter(lambda x: temp[x] == 3, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(three) == 1:
                n3 = 0
                n8 = 0
                n9 = 0
                for i in range(5):
                    if temp[i] == 3 and n3 != 1:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 8 and n8 != 1:
                        idx.append(i)
                        n8 += 1
                    elif temp[i] == 9 and n9 != 1:
                        idx.append(i)
                        n9 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 3 and self.cards[i].getNum() == 1:
                        o = i

                n3 = 0
                n8 = 0
                n9 = 0
                for i in range(5):
                    if temp[i] == 3 and n3 != 1 and i != o:
                        idx.append(i)
                        n3 += 1
                    elif temp[i] == 8 and n8 != 1:
                        idx.append(i)
                        n8 += 1
                    elif temp[i] == 9 and n9 != 1:
                        idx.append(i)
                        n9 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if temp.count(4) >= 2 and 2 in temp:
            result.append('살살이 (4 4 2)')
            index = (list(filter(lambda x: temp[x] == 4 or temp[x] == 2, range(len(temp)))))

            idx = []
            check_list = []

            n2 = 0
            n4 = 0
            for i in range(5):
                if temp[i] == 4 and n4 != 2:
                    idx.append(i)
                    n4 += 1
                elif temp[i] == 2 and n2 != 1:
                    idx.append(i)
                    n2 += 1

            made_index.append(idx)
            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            rest.append(self.check(check_list))

            made = True

        if 4 in temp and 6 in temp and 10 in temp:
            result.append('사륙장 (4 6 10)')
            index = (list(filter(lambda x: temp[x] == 4 or temp[x] == 6 or temp[x] == 10, range(len(temp)))))

            idx = []
            check_list = []
            n4 = 0
            n6 = 0
            n10 = 0

            for i in range(5):
                if temp[i] == 4 and n4 != 1:
                    idx.append(i)
                    n4 += 1
                elif temp[i] == 6 and n6 != 1:
                    idx.append(i)
                    n6 += 1
                elif temp[i] == 10 and n10 != 1:
                    idx.append(i)
                    n10 += 1

            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            made_index.append(idx)
            rest.append(self.check(check_list))

            made = True

        if 4 in temp and 7 in temp and 9 in temp:
            result.append('사칠구 (4 7 9)')
            index = (list(filter(lambda x: temp[x] == 4 or temp[x] == 7 or temp[x] == 9, range(len(temp)))))

            idx = []
            check_list = []
            n4 = 0
            n7 = 0
            n9 = 0

            for i in range(5):
                if temp[i] == 4 and n4 != 1:
                    idx.append(i)
                    n4 += 1
                elif temp[i] == 7 and n7 != 1:
                    idx.append(i)
                    n7 += 1
                elif temp[i] == 9 and n9 != 1:
                    idx.append(i)
                    n9 += 1

            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            made_index.append(idx)
            rest.append(self.check(check_list))

            made = True

        if temp.count(5) >= 2 and 10 in temp:
            result.append('꼬꼬장 (5 5 10)')
            index = (list(filter(lambda x: temp[x] == 5 or temp[x] == 10, range(len(temp)))))

            idx = []
            check_list = []

            n5 = 0
            n10 = 0
            for i in range(5):
                if temp[i] == 5 and n5 != 2:
                    idx.append(i)
                    n5 += 1
                elif temp[i] == 10 and n10 != 1:
                    idx.append(i)
                    n10 += 1

            made_index.append(idx)
            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            rest.append(self.check(check_list))

            made = True

        if 5 in temp and 6 in temp and 9 in temp:
            result.append('오륙구 (5 6 9)')
            index = (list(filter(lambda x: temp[x] == 5 or temp[x] == 6 or temp[x] == 9, range(len(temp)))))

            idx = []
            check_list = []
            n5 = 0
            n6 = 0
            n9 = 0

            for i in range(5):
                if temp[i] == 5 and n5 != 1:
                    idx.append(i)
                    n5 += 1
                elif temp[i] == 6 and n6 != 1:
                    idx.append(i)
                    n6 += 1
                elif temp[i] == 9 and n9 != 1:
                    idx.append(i)
                    n9 += 1

            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            made_index.append(idx)
            rest.append(self.check(check_list))

            made = True

        if 5 in temp and 7 in temp and 8 in temp:
            result.append('오리발 (5 7 8)')
            index = (list(filter(lambda x: temp[x] == 5 or temp[x] == 7 or temp[x] == 8, range(len(temp)))))

            eight = list(filter(lambda x: temp[x] == 1, range(len(temp))))

            idx = []
            check_list = []
            o = -1

            if len(eight) == 1:
                n5 = 0
                n7 = 0
                n8 = 0
                for i in range(5):
                    if temp[i] == 5 and n5 != 1:
                        idx.append(i)
                        n5 += 1
                    elif temp[i] == 7 and n7 != 1:
                        idx.append(i)
                        n7 += 1
                    elif temp[i] == 8 and n8 != 1:
                        idx.append(i)
                        n8 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))
            else:
                for i in range(5):
                    if temp[i] == 8 and self.cards[i].getNum() == 1:
                        o = i

                n5 = 0
                n7 = 0
                n8 = 0
                for i in range(5):
                    if temp[i] == 8 and n8 != 1 and i != o:
                        idx.append(i)
                        n8 += 1
                    elif temp[i] == 5 and n5 != 1:
                        idx.append(i)
                        n5 += 1
                    elif temp[i] == 7 and n7 != 1:
                        idx.append(i)
                        n7 += 1

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                made_index.append(idx)
                rest.append(self.check(check_list))

            made = True

        if temp.count(6) >= 2 and 8 in temp:
            result.append('쭉쭉팔 (6 6 8)')
            index = (list(filter(lambda x: temp[x] == 6 or temp[x] == 8, range(len(temp)))))
            eight = (list(filter(lambda x: temp[x] == 8, range(len(temp)))))

            if len(eight) == 1:
                idx = []
                check_list = []
                n6 = 0
                n8 = 0

                for i in range(5):
                    if temp[i] == 6 and n6 != 2:
                        idx.append(i)
                        n6 += 1
                    elif temp[i] == 8 and n8 != 1:
                        idx.append(i)
                        n8 += 1

                made_index.append(idx)

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                rest.append(self.check(check_list))

            else:
                idx = []
                check_list = []
                n6 = 0
                n8 = 0
                e = -1

                for i in range(5):
                    if temp[i] == 8 and self.cards[i].getNum() == 1:
                        e = i

                for i in range(5):
                    if temp[i] == 6 and n6 != 2:
                        idx.append(i)
                        n6 += 1
                    elif temp[i] == 8 and n8 != 1 and i != e:
                        idx.append(i)
                        n8 += 1

                made_index.append(idx)

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                rest.append(self.check(check_list))

            made = True

        if temp.count(7) >= 2 and 6 in temp:
            result.append('철철육 (7 7 6)')
            index = (list(filter(lambda x: temp[x] == 7 or temp[x] == 6, range(len(temp)))))

            idx = []
            check_list = []

            n7 = 0
            n6 = 0
            for i in range(5):
                if temp[i] == 7 and n7 != 2:
                    idx.append(i)
                    n7 += 1
                elif temp[i] == 6 and n6 != 1:
                    idx.append(i)
                    n6 += 1

            made_index.append(idx)
            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            rest.append(self.check(check_list))

            made = True

        if temp.count(8) >= 2 and 4 in temp:
            result.append('팍팍싸 (8 8 4)')
            index = (list(filter(lambda x: temp[x] == 8 or temp[x] == 4, range(len(temp)))))
            eight = (list(filter(lambda x: temp[x] == 8, range(len(temp)))))

            if len(eight) == 2:
                idx = []
                check_list = []
                n8 = 0
                n4 = 0

                for i in range(5):
                    if temp[i] == 8 and n8 != 2:
                        idx.append(i)
                        n8 += 1
                    elif temp[i] == 4 and n4 != 1:
                        idx.append(i)
                        n4 += 1

                made_index.append(idx)

                for i in range(5):
                    if i not in idx:
                        check_list.append(self.cards[i])

                rest.append(self.check(check_list))

            else:
                idx = []
                check_list = []
                n8 = 0
                n4 = 0
                e = -1

                for i in range(5):
                    if temp[i] == 8 and self.cards[i].getNum() == 1:
                        e = i

                if e != -1:
                    for i in range(5):
                        if temp[i] == 8 and n8 != 2:
                            idx.append(i)
                            n8 += 1
                        elif temp[i] == 4 and n4 != 1:
                            idx.append(i)
                            n4 += 1

                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))
                else:
                    for i in range(5):
                        if temp[i] == 8 and n8 != 2 and i != e:
                            idx.append(i)
                            n8 += 1
                        elif temp[i] == 4 and n4 != 1:
                            idx.append(i)
                            n4 += 1

                    made_index.append(idx)

                    for i in range(5):
                        if i not in idx:
                            check_list.append(self.cards[i])

                    rest.append(self.check(check_list))

            made = True

        if temp.count(9) >= 2 and 2 in temp:
            result.append('구구리 (9 9 2)')
            index = (list(filter(lambda x: temp[x] == 9 or temp[x] == 2, range(len(temp)))))

            idx = []
            check_list = []

            n9 = 0
            n2 = 0
            for i in range(5):
                if temp[i] == 9 and n9 != 2:
                    idx.append(i)
                    n9 += 1
                elif temp[i] == 2 and n2 != 1:
                    idx.append(i)
                    n2 += 1

            made_index.append(idx)
            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            rest.append(self.check(check_list))

            made = True

        if temp.count(10) >= 3:
            result.append('장장장 (10 10 10)')

            idx = []
            check_list = []
            ten = 0
            for i in range(5):
                if temp[i] == 10 and ten != 3:
                    idx.append(i)
                    ten += 1

            for i in range(5):
                if i not in idx:
                    check_list.append(self.cards[i])

            rest.append(self.check(check_list))
            made_index.append(idx)

            made = True

        if not made:
            print('노메이드')
            return [-1, '노메이드']
        else:   # return [족보 순위 + '메이드 결과'(result + rest) + [메이드 인덱스]]
            # 최고 메이드 찾기
            point = []
            print(rest)
            for i in range(len(rest)):
                point.append(pedigree.index(rest[i]))

            m = max(point)
            n = rest.index(pedigree[m])
            return [m, result[n]+' '+rest[n], made_index[n]]
