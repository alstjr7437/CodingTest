# 2023-01-12 문자열

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

# 1152 단어의 개수
# split으로 띄어쓰기로 문자 구분 후 len으로 갯수 확인
# result = input().split()
# print(len(result))

# 2908 상수
# a,b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# if a > b :
#     print(a)
# else :
#     print(b)

# 5622 다이얼
# a = input()
# sum = 0
# for i in range(len(a)):
#     if ord(a[i]) >= 65 and ord(a[i]) <= 67:
#         sum += 3
#     elif ord(a[i]) >= 68 and ord(a[i]) <= 70:
#         sum += 4
#     elif ord(a[i]) >= 71 and ord(a[i]) <= 73:
#         sum += 5
#     elif ord(a[i]) >= 74 and ord(a[i]) <= 76:
#         sum += 6
#     elif ord(a[i]) >= 77 and ord(a[i]) <= 79:
#         sum += 7
#     elif ord(a[i]) >= 80 and ord(a[i]) <= 83:
#         sum += 8
#     elif ord(a[i]) >= 84 and ord(a[i]) <= 86:
#         sum += 9
#     elif ord(a[i]) >= 87 and ord(a[i]) <= 90:
#         sum += 10
#     else :
#         sum += 11
# print(sum)

# 2941 크로아티아 알파벳
# for 문으로 i에 word를 넣으며 교체되는 함수
# word = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# a = input()
# for i in word :
#     a = a.replace(i, '*')  # input 변수와 동일한 이름의 변수
# print(len(a))

# 1316 그룹 단어 체커
# for문 안에 알고리즘 잘 깨닫기
# a = int(input())
# result = 0
# for i in range(a):
#     word = input()
#     no = 0
#     for j in range(len(word)-1):
#         if word[j] != word[j+1]:        # 문자가 연속으로 안될때
#             new = word[j+1:]            # 비교 글자 뒤로 문자를 생성
#             if new.count(word[j]) > 0:  # 생성된 문자와 비교해서 있다면 no를 +1
#                 no += 1
#     if no == 0 :                        # 뒤에 같은 문자가 없을시 결과를 +1
#         result+=1
# print(result)

