# 2022-12-31 반복문2, 함수
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


# 함수 부분

# 15596 정수 N개의 합
# 리스트의 sum 이용
# def solve(a):
#     return sum(a)
# for문 이용
# def solv(a):
#     b = 0
#     for i in a:
#         b+=i
#     return b

# 4673 셀프 넘버 ★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★★
# 1부터 10000까지 하는데 셀프넘버 구하기
# 66 = 66+ 6 + 6 = 78 이렇게 해서 78을 num에서 빼면서 안빼지는 숫자 구하기
# num = list(range(1,10001))
# result = []
# for i in num:
#     for j in str(i):
#         i += int(j)
#     if i <= 10000:
#         result.append(i)
# for i in set(result):
#     num.remove(i)
# for i in num:
#     print(i)

# 1065 한수
# 99까지는 모든 수가 한수 등차수열로 이루어짐 98 > 9 8 1로 등차수열
# 100이상 부터는 0번째 - 1번째 1 1번째 2번째 0 이므로 1 0 이므로 등차수열 X
# num = int(input())
# def re(n):
#     count = 0
#     for i in range(1, n+1):
#         num_list = list(map(int,str(i)))
#         if i < 100:
#             count+=1
#         elif num_list[0]-num_list[1] == num_list[1] - num_list[2]:
#             count+=1
#     return count
# print(re(num))