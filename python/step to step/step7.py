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
a = int(input())
count = 1
while a > count :
    a -= count
    count += 1
if count % 2 == 0:
    b = a
    c = count - a + 1
else :
    b = count - a + 1
    c = a
print(f"{b}/{c}")