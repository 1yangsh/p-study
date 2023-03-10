# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드


# 기본형
print(int)
print(float)

# 모든 속성 및 메소드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 10)
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))  # If 0 False, else True
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return f"Fruit Class Info : {self._name} {self._price}"

    def __add__(self, other):
        print("called >> __add__")
        return self._price + other._price

    def __sub__(self, other):
        print("called >> __sub__")
        return self._price - other._price

    # 대소 비교
    def __le__(self, other):
        print("called >> __le__")
        if self._price == other._price:
            return True
        else:
            return False

    def __ge__(self, other):
        print("called >> __ge__")
        if self._price >= other._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# 메직메소드를 모를 시,
print(s1._price + s2._price)

# 메직메소드 사용
print(s1 + s2)

# 매직메소드
print(s1 <= s2)
print(s1 >= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
