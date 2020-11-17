
print("[프로그래밍 언어]")


print("1. 자료형(data type)")
print("자료형이란 데이터의 성질을 나타내는 것으로 정수(int), 실수(float), 문자열(str)과 같은 형태가 있다.")
print("type() 함수를 이용해 데이터의 자료형을 알아볼 수 있다.")



print("2. 변수(variable)")
print("변수를 사용하여 계산하거나 다른 값을 대입할 수 있다.")

x = 10     # 초기화
print(x)   # x의 값 출력
x = 100    # 변수에 값 대입
print(x)

y = 3.14
print(x * y, type(x * y))

print("파이썬은 동적 언어로 분류되는데 동적이라 함은 변수의 자료형을 상황에 맞게 자동으로 결정한다는 뜻")



print("3. 리스트 (list)")
a = [1, 2, 3, 4, 5]       # 리스트 생성
print(a)

print(len(a))             # 리스트의 길이 출력
print(a[0])               # 첫 원소에 접근
print(a[4])               # 다섯 번째 원소에 접근

a[4] = 99
print(a)

print("원소에 접근할 때는 a[0] 처럼한다. []안의 수를 index(색인)라 하며 index는 0부터 시작함 (0이 첫번째 원소를 가리킴)")
print("파이썬의 list에는 Slicing(슬라이싱)이라는 편리한 기법이 있어 범위를 지정해 원하는 부분 list를 얻을 수 있다.")

print(a)
print(a[0:2])     # index 0부터 2까지 얻기 (2번째는 포함되지 않는다)
print(a[1:])      # index 1부터 끝까지 얻기
print(a[:3])      # 처음부터 index 3까지 얻기 (3번째는 미포함)
print(a[:-1])     # 처음부터 마지막 원소의 1개 앞까지 얻기 (마지막 원소만 제외)
print(a[:-2])     # 처음부터 마지막 원소의 2개 앞까지 얻기 (마지막 원소, 마지막 두번째 원소 제외)

print("list를 slicing 하려면 a[0:2]처럼 쓴다.")
print(a[0:2])     # a[0:2]는 index 0부터 1까지의 원소를 꺼낸다.

print("4. 딕셔너리(Dict)")


hap = 0
for i in range(10):
    hap = hap +1;
print(hap)


c = 0
for a in range(1, 3):
    for b in range(2, 5):
        c = c + 1
print(c)










