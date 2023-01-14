# 2023-01-14 기본 수학 1단계

# 1712 손익 분기점
a,b,c = map(int,input().split())
if b>=c:
    print(-1)
else :
    print(a//(c-b)+1)