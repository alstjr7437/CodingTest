# 2022-12-27 단계별 풀기 조건문

# 1330 숫자 비교하기
# A, B = map(int, input().split())
#
# if A > B :
#     print(">")
# elif A < B :
#     print("<")
# if A == B :
#     print("==")

# 9498 시험정석 받기
# A = int(input())
#
# if A >= 90 :
#     print("A")
# elif A >= 80 :
#     print("B")
# elif A >= 70 :
#     print("C")
# elif A >= 60 :
#     print("D")
# else :
#     print("F")

# 2753 윤년 문제
# A = int(input())
# if A % 4 == 0 and A % 100 != 0 or A % 400 == 0 :
#     print("1")
# else :
#     print("0")

# 14681 사분면 고르기
# x = int(input())
# y = int(input())
# if x > 0 and y > 0 :
#     print("1")
# elif x < 0 and y > 0 :
#     print("2")
# elif x < 0 and y < 0 :
#     print("3")
# else :
#     print("4")

# 2884 알람시계
# a,b = map(int, input().split())
# if b < 45 and a > 0:
#     print(a-1, b+15)
# elif b < 45 and a == 0 :
#     print(23, b+15)
# else :
#     print(a, b-45)

# 2525 오븐 시계
# a,b = map(int, input().split())
# c = int(input())
#
# a += c // 60
# b += c % 60
# if b >= 60 :
#     a += 1
#     b -= 60
# if a >= 24 :
#     a -= 24
# print(a,b)

# 2480 주사위 세개
# a,b,c = map(int, input().split())
# if a == b or a == c or b == c :
#     if a == b and a == c and b == c :
#         print(10000 + a * 1000)
#     elif a == b:
#         print(1000 + a * 100)
#     elif a == c:
#         print(1000 + a * 100)
#     elif b == c:
#         print(1000 + b * 100)
# else :
#     if a > b and a > c:
#         print(a * 100)
#     elif b > a and b > c:
#         print(b * 100)
#     elif c > a and c > b:
#         print(c * 100)