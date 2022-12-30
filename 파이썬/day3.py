#2022-12-30
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

# 15552 빠른 A+B 시간제한 1초
# import sys
# count = int(sys.stdin.readline())
# for i in range(count):
#     a,b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 11021 A+B-7
count = int(input())
for i in range(1, count+1):
     a,b = map(int, input().split())
     print(f"Case #{i}: {a+b}")

# 다음날