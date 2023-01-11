# 2023-01-11 문자열

# 11654 아스키코드
# print(ord(input()))

# 11720 숫자의 합
# a = int(input())
# print(sum(map(int, input())))

# 10809 알파벳 찾기
# num에 아스키코드 값 넣어두고 쭉 나열해놓기
# find로 찾아서 아스키코드에 맞는값 일 시 index를 출력하고 없으면 -1을 자동으로 출력한다.
# alpha = input()
# num = list(range(97,123))
# for i in num:
#     print(alpha.find(chr(i)), end=' ')

# 2675 문자열 반복
# a와 b로 잘라서 a는 몇번 반복할지 num으로 바꾸고 re에 결과값이므로 반복을 곱해서 출력한다.
# a = int(input())
# for i in range(a):
#     a,b = input().split()
#     num = int(a)
#     re = ''
#     for j in range(len(b)):
#         re += b[j] * num
#     print(re)

# 1157 단어 공부
# upper로 대소문자 구분 없애기, set으로 어떤 단어들 있는지 저장해두기
# count로 몇번인지 갯수 세서 리스트에 넣기
# alpha = input().upper()
# al = list(set(alpha))
# count = []
# for i in al:
#     count.append(alpha.count(i))
# if count.count(max(count)) == 1 :
#     a = count.index(max(count))
#     print(al[a])
# else :
#     print('?')