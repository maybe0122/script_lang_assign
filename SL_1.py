# Script Language assignment-1

# 1-9 (직사각형 넓이와 둘레)
width = 4.5
height = 7.9
area = width * height
round = 2 * (width + height)

print("1-9")
print(area, round)
print()

# 1-10 (평균 속력)
kmph = 14 / ((45*60 + 30) / 3600)
mph = kmph / 1.6

print('1-10')
print(mph)
print()

# 1-11 (인구 수 프로젝트)
year_to_sec = 365*24*60*60
popularity = 312032486
birth = year_to_sec // 7
death = year_to_sec // 13
immigrant = year_to_sec // 45

print('1-11')
for i in range(1, 5 + 1):  # 매 5년마다 인구수 출력(최대 25년)
    print(5*i, "년 후 인구 : ", popularity + 5 * i * (birth - death + immigrant))
print()

# 2-4 (파운드 킬로그램 변환)
pounds_to_kg = 0.454
pounds = eval(input("파운드 값을 입력하세요: "))
# print(pounds, "파운드는 ", pounds * pounds_to_kg, "킬로그램입니다.")
print('2-4')
print(f'{pounds} 파운드는 {pounds * pounds_to_kg} 킬로그램입니다.')
print()

# 2-5 (금융 애플리케이션: 팁 계산)
subtotal, tip_percent = eval(input('소계와 팁 비율을 입력하세요: '))
tip = subtotal * (tip_percent / 100)
total = subtotal + tip
print('2-5')
print(f'팁은 {tip:.2f}이고 총액은 {total:.2f}입니다.')
print()

# 2-6 (정수의 자리수 합산하기)
num = eval(input('0과 1000 사이의 숫자를 입력하세요: '))
result = 0
while num != 0:
    result += num % 10
    num = num // 10


print('2-6')
print(f'이 자릿수들의 합은 {result} 입니다.')
print()


# 2-7 (년과 일 수 계산하기)
min = eval(input('분에 대한 숫자를 입력하세요: '))
day = min // (60 * 24)
year = day // 365
print('2-7')
print(f'{min}분은 약 {year}년 {day % 365}일 입니다.')
print()

# 2-9 (과학: 체감온도)
ta = eval(input('화씨 -58F 와 41F 사이의 온도를 입력하세요: '))
v = eval(input('풍속을 시간 당 마일 단위로 입력하세요: '))
twc = 35.74 + 0.6215 * ta - 35.75 * (v ** 0.16) + 0.4275 * ta * (v ** 0.16)
print('2-9')
print(f'체감온도는 {twc:.5f} 입니다.')
print()

# 2-11 (금융 애플리케이션: 약정 금액)
value = eval(input('약정 금액을 입력하세요: '))
rate = eval(input('연이율(%)을 입력하세요: '))
years = eval(input('약정기간(년)을 입력하세요: '))
month_rate = rate / (12 * 100)
deposit = value / ((1 + month_rate) ** (years * 12))
print('2-11')
print(f'월 납입금은 {deposit}입니다.')
print()

# 2-17 (건강 애플리케이션: BMI 계산하기)
w = eval(input('몸무게를 파운드로 입력하세요: '))
h = eval(input('키를 인치로 입력하세요: '))
BMI = (w * 0.45359237) / ((h * 0.0254)**2)
print('2-17')
print(f'BMI는 {BMI:.4f} 입니다.')
print()