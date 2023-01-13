# 2022-12-30 반복문1
# 2739 구구단
# a = int(input())
#
# for i in range(1,10):
#     print(a, "*", i, "=",a * i , sep=" ")

# 10950 a+b-3
# count = int(input())
# num = []
# for i in range(count):
#     a,b = map(int, input().split())
#     num.append(a+b)
# for i in range(count):
#     print(num[i])

# 8393 합
# a = int(input())
# num = 0
# for i in range(a+1):
#     num += i
# print(num)

# 25304 영수증
# money = int(input())
# count = int(input())
# sum = 0
# for i in range(count):
#     a,b = map(int,input().split())
#     sum += a*b
# if sum == money :
#     print("Yes")
# else :
#     print("No")

# 15552 빠른 A+B ★★★★★시간제한 1초
# import sys
# count = int(sys.stdin.readline())
# for i in range(count):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 11021 A+B-7
# count = int(input())
# for i in range(1, count+1):
#      a,b = map(int, input().split())
#      print(f"Case #{i}: {a+b}")

# 11022 A+B-8
# count = int(input())
# for i in range(1, count+1):
#      a,b = map(int, input().split())
#      print(f"Case #{i}: {a} + {b} = {a+b}")

# 2438 별찍기1
# a = int(input())
# for i in range(1,a+1):
#     for j in range(i):
#         print("*", end='')
#     print()

# 2439 별찍기2
# a = int(input())
# for i in range(1,a+1):
#     for z in range(a-i):
#         print(" ", end='')
#     for j in range(i):
#         print("*", end='')
#     print()

# 다른 방식
# a = int(input())
# for i in range(1, a+1):
#     print(" " * (a-i), "*" * i, sep="", end='\n')

# 10952 A+B-5
# while 1:
#     a,b = map(int,input().split())
#     if a == 0 and b == 0:
#         break
#     print(a+b)

# 10951 A+B-4 ★★★★★try except 부분!!
# while 1:
#     try :
#         a, b = map(int, input().split())
#         print(a + b)
#     except:
#         break

# 1110 더하기 사이클
# n = int(input())
# num = n
# count = 0
# while 1 :
#     a = num // 10
#     b = num % 10
#     c = (a + b) % 10
#     num = (b * 10) + c
#     count+=1
#     if num == n :
#         break
# print(count)
