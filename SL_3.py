import random

# 4-1 (대수: 이차방정식 풀기)
def ex4_1():
    print('4-1')
    for _ in range(3):
        a, b, c = eval(input('A, B, C를 입력하세요: '))
        D = b**2 - (4 * a * c)

        r1 = (-b + D**0.5) / (2 * a)
        r2 = (-b - D**0.5) / (2 * a)

        if D > 0:
            print(f'실근은 {r1:.6f}과 {r2:.6f} 입니다.')
        elif D == 0:
            print(f'실근은 {r1} 입니다.')
        else:
            print('이 방정식은 실근이 존재하지 않습니다.')

# 4-24 (게임: 카드 뽑기)
def ex4_24():
    print('4-24')
    num = random.randint(1, 52)

    if (num - 1) // 13 == 0:
        pattern = '클로버'
    elif (num - 1) // 13 == 1:
        pattern = '다이아몬드'
    elif (num - 1) // 13 == 2:
        pattern = '하트'
    else:
        pattern = '스페이드'

    if num % 13 == 0:
        i = 'K'
    elif num % 13 < 11:
        i = num % 13
    elif num % 13 < 12:
        i = 'J'
    else:
        i = 'Q'

    print(f'당신이 뽑은 카드는 {pattern} {i} 입니다.')

# 4-27 (기하: 삼각형 내부 점)
def ex4_27():
    print('4-27')
    for _ in range(2):
        x, y = eval(input('점의 x와 y 좌표값을 입력하세요: '))


        if x < 0 or x > 200 or y < 0 or y > 100:
            print('점은 삼각형의 내부에 있지 않습니다.')
        else:
            f = (0 - 100)/(200 - 0) * x + 100
            if f > y:
                print('점은 삼각형의 내부에 있습니다.')
            else:
                print('점은 삼각형의 내부에 있지 않습니다.')

# 5-39 (금융 어플: 매출액 구하기)
def ex5_39(): # 수정
    print('5-39')
    basic = 5000000
    goal = 30000000
    take = 1
    commission = 0
    while basic + commission < goal:
        take += 1
        if take > 10000000:
            commission = basic * (-0.06) + take * 0.12
        elif take > 5000000:
            commission = basic * (-0.02) + take * 0.1
        else:
            commission = take * 0.08

    print(f'목표 달성을 위한 최소 매출액: {take}')

# 5-42 (몬테카를로 시뮬레이션)
def ex5_42():
    print('5-42')
    count = 0
    for i in range(1000000):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1

        if x < 0:
            count += 1
        elif 0 <= x <= 1 and 0 <= y <= 1:
            y1 = y + x
            if y1 <= 1:
                count += 1

    print(f'홀수 번호의 영역에 점이 있을 확률: {count / 1000000}')

# 6-3 (대칭수)
def reverse(number):
    n = str(number)
    result = int(n[::-1])
    return result

def isPalindrome(number):
    return number == reverse(number)

def ex6_3():
    print('6-3')
    number = eval(input('정수를 입력해주세요: '))

    if isPalindrome(number):
        print(f'{number}는 대칭수 입니다.')
    else:
        print(f'{number}는 대칭수가 아닙니다.')

# 6-4 (정수 역순 출력)
def ex6_4():
    print('6-4')
    number = eval(input('정수를 입력해주세요: '))
    print(reverse(number))

# 6-5 (3개 숫자 정렬)
def displaySortedNumbers(num1,num2, num3):
    if num1 > num2:
        num1, num2 = num2, num1
    if num2 > num3:
        num2, num3 = num3, num2
    if num1 > num2:
        num1, num2 = num2, num1
    print(f'정렬된 숫자는 {num1} {num2} {num3} 입니다.')

def ex6_5():
    print('6-5')
    n1, n2, n3 = eval(input('세 개의 수를 입력하세요: '))
    displaySortedNumbers(n1, n2, n3)

# 6-12 (문자 출력)
def printChars(ch1, ch2, numberPerLine):
    count = 1
    for i in range(ord(ch1), ord(ch2)+1):
        if count % numberPerLine == 0:
            print(chr(i))
        else:
            print(chr(i), end=' ')
        count += 1

def ex6_12():
    print('6-12')
    printChars('1', 'Z', 10)

# 6-13 (합 급수)
def ex6_13():
    sum = 0
    print('6-13')
    print('\ti\t\tm(i)')
    for i in range(1, 21):
        sum += i/(i+1)
        print(f'\t{i}\t\t{sum}')

# 15-3 (재귀함수: 최대공약수)
def gcd(m, n):
    if m % n == 0:
        return n
    return gcd(n, m % n)

def ex15_3():
    print('15-3')
    n, m = eval(input('두 정수를 입력하세요: '))
    print(f'{n}와 {m}의 최대공약수는 {gcd(n, m)}입니다.')

# 15-4 (재귀함수: 수열의 합)
def m(i):
    if i == 1:
        return 1
    return 1/i + m(i-1)

def ex15_4():
    print('15-4')
    print('\ti\t\tm(i)')
    for i in range(1, 10+1):
        print(f'\t{i}\t\t{m(i)}')

# 15-18(하노이 타워)
count_move = 0

def ex15_18():
    print('15-18')
    n = eval(input('디스크의 개수를 입력하세요: '))
    # 해결 방법을 재귀적으로 찾는다.
    print('옮기는 순서는 다음과 같습니다:')
    moveDisks(n, 'A', 'B', 'C')
    print(f'디스크 이동 횟수: {count_move}')

def moveDisks(n, fromTower, toTower, auxTower):
    global count_move
    count_move += 1
    if n == 1:  # 정지 조건
        print('디스크 ', n, '을 / 를 ', fromTower, '에서 ', toTower, '로 옮긴다.')
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print('디스크 ', n, '을 / 를 ', fromTower, '에서 ', toTower, '로 옮긴다.')
        moveDisks(n - 1, auxTower, toTower, fromTower)

# 15-19(10진수를 2진수로)
def ex15_19():
    print('15-19')
    num = eval(input('정수를 입력해주세요: '))
    print(f'{num}의 이진수: {decimalToBinary(num)}')

def decimalToBinary(value):
    if value == 0:
        return ''
    else:
        return decimalToBinary(value // 2) + str(value % 2)

# 15-20(10진수를 16진수)
def ex15_20():
    print('15-20')
    num = eval(input('정수를 입력해주세요: '))
    print(f'{num}의 16진수: {decimalToHex(num)}')

def decimalToHex(value):
    if value == 0:
        return ''
    else:
        if value % 16 == 10:
            r = 'A'
        elif value % 16 == 11:
            r = 'B'
        elif value % 16 == 12:
            r = 'c'
        elif value % 16 == 13:
            r = 'D'
        elif value % 16 == 14:
            r = 'E'
        elif value % 16 == 15:
            r = 'F'
        else:
            r = str(value % 16)
        return decimalToHex(value // 16) + r


ex4_1()
ex4_24()
ex4_27()
ex5_39()
ex5_42()
ex6_3()
ex6_4()
ex6_5()
ex6_12()
ex6_13()
ex15_3()
ex15_4()
ex15_18()
ex15_19()
ex15_20()
