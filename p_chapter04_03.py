# Chapter04-03
# 시퀀스형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque])
# 플랫(Flat: 한 개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)

# 해시 테이블
# Key에 Value를 저장하는 구조  __dict__
# 파이썬 dict 해쉬 테이블 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구죠
# key 값을 해싱 함수 -> 해싱 주소 -> key 에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값을 확인 (고유 값)
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])
print(hash(t1))  # hash() 안에는 불변형이여야함.
# print(hash(t2))  # 리스트는 가변이라 해쉬 함수를 사용할 수 없다. (예외)

# Dict SetDefault 예제
source = (
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5"),
)

new_dict1 = {}
new_dict2 = {}

# No use SetDefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]
print(new_dict1)

# Use SetDefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)  # key 값이 중복 될 경우 처리가 가능
print(new_dict2)


# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3)  # 중복 처리가 안됨

print()
print()
