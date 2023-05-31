# Script Language assignment-2
import math
import time
import random

def distance(x1, y1, x2, y2):
    d = 6370.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * \
                      math.cos(math.radians(x2)) * math.cos(math.radians(y1 - y2)))
    return d

def area(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    a = (s * (s - l1) * (s - l2) * (s - l3)) ** 0.5
    return a

# 2-14 (기하 삼각형의 넓이)
print('2-14')
x1, y1, x2, y2, x3, y3 = eval(input('삼각형의 세 꼭짓점을 입력하세요: '))
s = math.fabs((x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)) / 2

print(f'삼각형의 넓이는 {s:.1f} 입니다.')
print()

# 3-2 (기하학: 대권 거리)
print('3-2')
dx1, dy1 = eval(input('첫 번째 점(위도와 경도)을 60분법 각으로 입력하세요.: '))
dx2, dy2 = eval(input('두 번째 점(위도와 경도)을 60분법 각으로 입력하세요.: '))

d = distance(dx1, dy1, dx2, dy2)

print(f'두 점 사이의 거리는 {d} km입니다.')
print()

# 3-3 (지리학: 넓이 추정하기)
print('3-3')
cx1, cy1 = eval(input('광주광역시 : '))
cx2, cy2 = eval(input('부산광역시 : '))
cx3, cy3 = eval(input('강원+강릉시 : '))
cx4, cy4 = eval(input('서울특별시 : '))

l1 = distance(cx1, cy1, cx2, cy2)
l2 = distance(cx1, cy1, cx3, cy3)
l3 = distance(cx2, cy2, cx3, cy3)
l4 = distance(cx2, cy2, cx4, cy4)
l5 = distance(cx3, cy3, cx4, cy4)

s1 = area(l1, l2, l3)
s2 = area(l3, l4, l5)
ss = s1 + s2

print(f'네 도시에 의해 둘러 쌓인 넓이는 {ss:.1f} 입니다.')
print()

# 3-6 (아스키 코드의 문자 찾기)
print('3-6')
code = eval(input('ASCII 코드를 입력하세요: '))

print(f'문자는 {chr(code)}입니다.')

# 3-7 (랜덤 문자)
print('3-7')
print(chr(ord('A') + int(time.time()) % 26))
print()

# 3-8 (금융 애플리케이션: 급여)
print('3-8')
name = input('사원 이름을 입력하세요: ')
hour = eval(input('주 당 근무시간을 입력하세요: '))
pay = eval(input('시간 당 급여를 입력하세요: '))
r1 = eval(input('원천징수세율을 입력하세요: '))
r2 = eval(input('지방세율을 입력하세요: '))

tex1 = pay*hour*r1
tex2 = pay*hour*r2

print('사원 이름: ', name)
print('주당 근무시간: ', hour)
print('임금: ', pay)
print('총 급여:', pay*hour)
print(f"""
공제:
\t원천징수세({r1*100}%): {tex1:.0f}
\t주민세({r2*100}%): {tex2:.0f}
\t총 공제: {tex1 + tex2:.0f}
공제 후 급여: {pay*hour - (tex1 + tex2):.0f}
""")

# 10-2(입력된 숫자 역순 정렬)
print('10-2')
s = input('정수 리스트 입력 : ')
item = s.split()
numbers = [eval(x) for x in item]
numbers.reverse()
for i in numbers:
    print(i, end=' ')
print('\n')

# Ref. 10-2
print('Ref. 10-2')
print(f'lst의 원소의 개수 {len(numbers)}')
print(f'lst의 첫 번째 원소의 인덱스 {numbers.index(30)}, 마지막 원소의 인덱스 {numbers.index(0)}')
print(f'lst[2]의 값 : {numbers[2]}, lst[-2]의 값 {numbers[-2]}')

# 10-3(숫자의 빈도수)
print('10-3')
integer = list(map(int, input('1과 100 사이의 정수를 입력하세요: ').split()))
count = [0 for _ in range(101)]

for v in integer:
    count[v] += 1

for v in range(1, len(count)):
    if count[v] > 0:
        print(f'{v} - {count[v]}번 나타납니다.')

# Ref. 10-3
print('Ref. 10-3')
def ex10_3():
    integer = [30, 1, 2, 1, 0]
    integer.append(40)
    print(integer)
    integer.insert(1, 43)
    print(integer)
    integer.extend([1, 43])
    print(integer)
    integer.pop(1)
    print(integer)
    integer.pop()
    print(integer)
    integer.sort()
    print(integer)
    integer.reverse()
    print(integer)
    random.shuffle(integer)
    print(integer)

ex10_3()
print()

# 10-4 (점수 분석하기)
print('10-4')
int_list = list(map(int, input('정수를 입력하세요: ').split()))
average = 0

for v in int_list:
    average += v

average /= len(int_list)

count_big, count_small = 0, 0

for v in int_list:
    if average > v:
        count_small += 1
    elif average < v:
        count_big += 1

print(f'평균 {average:.1f} 보다 큰 숫자는 {count_big} 개, 작은 숫자는 {count_small} 개 입니다.')
print()

# Ref. 10-4
print('Ref. 10-4')
print(f'lst.index(1) : {int_list.index(1)}')
print(f'lst.count(1) : {int_list.count(1)}')
print(f'len(lst) : {len(int_list)}')
print(f'max(lst) : {max(int_list)}')
print(f'min(lst): {min(int_list)}')
print(f'sum(lst) : {sum(int_list)}')

# 10-5 (고유 숫자 출력하기)
print('10-5')
list1 = list(map(int, input('10 개의 숫자를 입력하세요: ').split()))
list2 = []

for v in list1:
    if v not in list2:
        list2.append(v)

print('중복을 제거한 고유한 숫자:', end=' ')
for v in list2:
    print(v, end=' ')
print('\n')

# Ref. 10-5
print('Ref. 10-5')
r1 = [30, 1, 2, 1, 0]
r2 = [1, 21, 13]

for v in r1:
    if v not in r2:
        r2.append(v)

print(f'list1 + list2 : {r1 + r2}')
print(f'2 * list1 : {2 * r1}')
print(f'list2 * 2 : {r2 * 2}')
print(f'list1[1:3] : {r1[1:3]}')
print(f'list1[3] : {r1[3]}')

# 10-8(가장 작은 원소의 인덱스 찾기)
print('10-8')
list_1 = list(map(int, input('정수 리스트를 입력하세요: ').split()))

def indexOfSmallestElement(lst):
    m = min(lst)
    return lst.index(m)

print(f'가장 작은 원소의 인덱스 : {indexOfSmallestElement(list1)}')

# 10-15(정렬되었는가?)
print('10-15')

def isSorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True

while(True):
    list_2 = list(map(int, input('정수 리스트를 입력하세요: ').split()))

    if isSorted(list_2):
        print('리스트는 이미 정렬되어 있습니다.')
        break
    else:
        print('리스트는 정렬되어 있지 않습니다.')

# 10-19(게임: 콩 기계)
print('10-19')
ball = eval(input('떨어뜨릴 공의 개수를 입력하세요: '))
machine = eval(input('콩 기계의 슬롯 개수를 입력하세요: '))

def ex(Nball, Nslots):
    slots = [0 for _ in range(Nslots)]
    for i in range(Nball):
        slots[path(Nslots)] += 1
    maxHeight = max(slots)
    for h in range(maxHeight, 0, -1):
        for i in range(len(slots)):
            if slots[i] < h:
                print(' ', end='')
            else:
                print('0', end='')
        print()

def path(Nslots):
    index = 0
    for i in range(Nslots - 1):
        if random.random() < 0.5:
            print('L', end='')
        else:
            print('R', end='')
            index += 1
    print()
    return index-1

ex(ball, machine)

# 11-1(열별 원소 합하기)
print('11-1')
def ex11_1():
    matrix = []
    for i in range(3):
        matrix.append(list(map(eval, input(f'3x4 행렬의 행 {i} 번에 대한 원소를 입력하세요: ').split())))
    for j in range(4):
        print(f'열 {j}번 원소의 총합은 {sumColumn(matrix, j)} 입니다.')

def sumColumn(m, columnIndex):
    sum = 0
    for i in range(len(m)):
        sum += m[i][columnIndex]
    return sum

ex11_1()

# 14-2 (숫자 빈도수 세기)
print('14-2')
def find():
    list_3 = list(map(int, input('정수 리스트를 입력하세요: ').split()))
    count = {}
    for n in list_3:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    maxCount = max(count.values())
    for k, v in count.items():
        if v == maxCount:
            print(k, end=' ')
    print()

for _ in range(2):
    find()

# 11-27(열 정렬하기)
print('11-27')

def test11_27():
    matrix = []
    row = 3
    col = 3
    print(f'{row} x {col} 행렬을 한 행씩 입력하세요:')
    for _ in range(row):
        matrix.append(list(map(eval, input().split())))
    sortColunms(matrix)

def sortColunms(m):
    for j in range(3):
        for _ in range(2):
            for i in range(1, 3):
                if m[i-1][j] > m[i][j]:
                    m[i-1][j], m[i][j] = m[i][j], m[i-1][j]

    print('열 정렬된 리스트는 다음과 같습니다.')
    for i in range(3):
        for j in range(3):
            print(m[i][j], end=' ')
        print()

test11_27()

# 11-34 (기하학: 최우하단 점)
print('11-34')

def test11_34():
    points = list(map(eval, input('6개의 점을 입력하세요: ').split()))
    result = []
    result.extend(getRightmostLowsetPoint(points))
    print(f'최우측하단의 점은 ({result[0]}, {result[1]})')

def getRightmostLowsetPoint(points):
    target = []
    map = [[] for _ in range(4)]    # 몇 사분면 점인지 저장하는 리스트 map

    # 사분면 판단
    for i in range(0, len(points), 2):
        if points[i] == 0:                          # y 축
            if points[i+1] >= 1:
                map[0].extend([points[i], points[i+1]])
            else:
                map[3].extend([points[i], points[i + 1]])
        elif points[i+1] == 0:                      # x 축
            if points[i] >= 0:
                map[3].extend([points[i], points[i + 1]])
            else:
                map[2].extend([points[i], points[i + 1]])
        elif points[i] > 0:
            if points[i+1] > 0:                     # 1사분면
                map[0].extend([points[i], points[i + 1]])
            else:                                   # 4사분면
                map[3].extend([points[i], points[i + 1]])
        else:                                       # 2사분면
            if points[i+1] > 0:
                map[1].extend([points[i], points[i + 1]])
            else:                                   # 3사분면
                map[2].extend([points[i], points[i + 1]])

    # 최하단 점 판별 : 우선순위 4 > 1 == 3 > 2, 같은 사분면이면 거리순
    if len(map[3]) > 0:
        index = maxdistance(map[3], 4)
        target.extend([map[3][index], map[3][index+1]])
    elif len(map[0]) > 0 or len(map[2]) > 0:
        a = maxdistance(map[0], 1)
        b = maxdistance(map[2], 3)

        if a == -1:
            target.extend([map[2][b], map[2][b + 1]])
        elif b == -1:
            target.extend([map[0][a], map[0][a + 1]])
        else:
            if (map[2][b]**2 + map[2][b+1]**2) ** 0.5 > (map[0][a]**2 + map[0][a+1]**2)**0.5:
                target.extend([map[2][b], map[2][b + 1]])
            else:
                target.extend([map[0][a], map[0][a + 1]])
    else:
        index = maxdistance(map[1], 2)
        target.extend([map[1][index], map[1][index+1]])


    return target

def maxdistance(list, a):
    long = []
    if len(list) == 0:
        return -1

    for i in range(0, len(list), 2):
        long.append((list[i] ** 2 + list[i + 1] ** 2) ** 0.5)

    if a != 2:
        m = max(long)
        return long.index(m) * 2
    else:
        m = min(long)
        return long.index(m) * 2


test11_34()