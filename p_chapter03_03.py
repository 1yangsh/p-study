# Chapter03-03
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)
# 클래스안에 정의할 수 있는 특별한(Built-in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 두 점 사이의 거리 구하기
# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng_1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(l_leng_1)


# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple("Point", "x y")

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)
print(pt3[0], pt4[1])
print(pt3.x, pt4.y)

l_leng_2 = sqrt((pt3[0] - pt4[0]) ** 2 + (pt3[1] - pt4[1]) ** 2)
l_leng_3 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng_2, l_leng_3)


# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])  # 1
Point2 = namedtuple("Point", "x, y")  # 2
Point3 = namedtuple("Point", "x y")  # 3
Point4 = namedtuple("Point", "x, y, x, class", rename=True)  # default = False

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {"x": 75, "y": 55}


# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point1(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4)
print(p5)

# 사용
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p3
print(x, y)


# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)
print(p4)

# _field() : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)


# _asdict() : Ordered Dict 반환
print(p1._asdict())
print(p4._asdict())


# 실 사용 실습
# 반 20 명, 4 개의 반 (A,B,C,D)

Classes = namedtuple("Classes", ["rank", "number"])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
students2 = [
    Classes(rank, number)
    for rank in "A B C D"
    for number in [str(n) for n in range(1, 21)]
]

print(students2)


# 출력
for s in students2:
    print(s)
