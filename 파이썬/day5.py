# 2023-01-10 1차원 배열

# 10807 개수 세기
# a = int(input())
# num = list(map(int, input().split()))
# search = int(input())
# print(num.count(search))

# 10871 X보다 작은 수
# a,b = map(int,input().split())
# num = list(map(int, input().split()))
# for i in range(a):
#     if num[i] < b :
#         print(num[i], end=' ')

# 10818 최소, 최대
# max()와 min()활용 X
# a = int(input())
# num = list(map(int, input().split()))
# max,min = num[0],num[0]
# for i in range(a):
#     if max < num[i]:
#         max = num[i]
#     if min > num[i]:
#         min = num[i]
# print(min,max)

# 2562 최댓값
# num = []
# maxnum = 0
# count = 0
# for i in range(9):
#     num.append(int(input()))
#     if maxnum < num[i]:
#         maxnum = num[i]
#         count = num.index(num[i])+1
# print(max,count, sep="\n")

# # 또는
# print(max(num), num.index(max(num))+1 , sep="\n")

# 5597 과제 안 내신 분
# max와 min 활용하기
# num = []
# for i in range(1,31):
#     num.append(i)
# for i in range(28):
#     a = int(input())
#     num.remove(a)
# print(min(num))
# print(max(num))

# 3052 나머지
# set을 이용해서 중복 제거하기!
# a = 42
# num = []
# for i in range(10):
#     num.append(int(input())%a)
# print(len(set(num)))

# 1546 평균
# new로 하여서 double로 바뀌도록 하기
# a = int(input())
# score = list(map(int, input().split()))
# new = []
# for i in range(a):
#     new.append(score[i] / max(score) * 100)
# print(sum(new) / len(new))

# 8958 OX 퀴즈
# score 부분과 sum 부분의 관계 잘 생각하기 (score은 O가 여러번 일 때 2점 더 해지고 그런 부분임 sum은 합계 점수 부분)
# a = int(input())
# for i in range(a):
#     ox = input()
#     score = 0
#     sum = 0
#     for i in range(len(ox)):
#         if ox[i] == 'O':
#             score += 1
#             sum += score
#         else :
#             score = 0
#     print(sum)

# 4344 평균은 넘겠지
# .3f와 round의 차이점 .000까지 나오는 부분이 다름, sum(score[1:])는 score 2번째 부터 쭉 더하는거
# a = int(input())
# for i in range(a):
#     score = list(map(int,input().split()))
#     avg = sum(score[1:]) / score[0]
#     count = 0
#     for j in range(1, score[0]+1):
#         if avg < score[j]:
#             count += 1
#     b = count/score[0] * 100
#     print('%.3f'%b,end='%\n')
