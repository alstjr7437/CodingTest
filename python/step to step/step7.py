# 2023-01-14 ~ (부경대 면접으로 인해 한문제씩)
# 기본 수학 1단계

# 1712 손익 분기점
# a,b,c = map(int,input().split())
# if b>=c:
#     print(-1)
# else :
#     print(a//(c-b)+1)

# 2292 벌집
# a = int(input())
# home = 1
# count = 1
# while a > home :
#     home += count * 6
#     count += 1
# print(count)

# 1193 분수 찾기
# a = int(input())
# count = 1
# while a > count :
#     a -= count
#     count += 1
# if count % 2 == 0:
#     b = a
#     c = count - a + 1
# else :
#     b = count - a + 1
#     c = a
# print(f"{b}/{c}")

# 2869 달팽이 올라가기
# a,b,v = map(int,input().split())
# k = (v-b)/(a-b)
# if k == int(k) :
#     k = int(k)
# else :
#     k = int(k) + 1
# print(k)

# 10250 호텔 방
# a = int(input())
# for i in range(a):
#     h, w, n = map(int, input().split())
#     room = n // h + 1
#     floor = n % h
#     if floor == 0 :
#         room = n // h
#         floor = h
#     print(f'{floor * 100 + room}')

# 2775 부녀회장
# a = int(input())
# for i in range(a):
#     k = int(input())
#     n = int(input())
#     f0 = []
#     for j in range(1,n+1):
#         f0.append(j)
#     for j in range(k):
#         for b in range(1, n):
#             f0[b] += f0[b-1]
#     print(f0[-1])

# 2839 설탕 배달
# a = int(input())
# count = 0
#
# while a >= 0 :
#     if a % 5 == 0 :
#         count += (a // 5)
#         print(count)
#         break
#     a -= 3
#     count += 1
# else :
#     print(-1)

# 10757 큰 수 A + B
# 파이썬이라 오버플로우로 터지지 않음
# a, b = map(int,input().split())
# print(a+b)