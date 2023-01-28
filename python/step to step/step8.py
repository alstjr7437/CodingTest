# 2023-01-28 ~ (알고리즘 배우기 전에는 한문제씩 하기)
# 기본 수학 2단계

# 1978 소수찾기
a = int(input())
num = list(map(int, input().split()))
result = 0
for i in range(a):
    no = 0
    if num[i] > 1 :
        for j in range(2, num[i]):
            if num[i] % j == 0:
                no += 1
        if no == 0 :
            result += 1
print(result)