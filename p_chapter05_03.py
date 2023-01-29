# Chapter05-03
# 일급 함수(일급 객체)
# 클로저 기초
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# Clouser 사용
def clouser_ex1():
    # Free Variable
    # 클로저 영역
    series = []

    def averager(v):
        series.append(v)
        print(f"inner >> {series} / {len(series)}")
        return sum(series) / len(series)

    return averager


avg_clouser1 = clouser_ex1()
print(avg_clouser1)
print(avg_clouser1(10))
print(avg_clouser1(30))
print(avg_clouser1(50))

print()
print()

# function inspection
print(dir(avg_clouser1))
print()
print(dir(avg_clouser1.__code__))
print()
print(avg_clouser1.__code__.co_freevars)
print(avg_clouser1.__closure__[0].cell_contents)

print()
print()

# 잘못된 클로저 사용
def clouser_ex2():
    # Free Variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_clouser2 = clouser_ex2()
# print(avg_clouser2(10))  # 예외


def clouser_ex3():
    # Free Variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_clouser3 = clouser_ex3()
print(avg_clouser3(15))
print(avg_clouser3(35))
print(avg_clouser3(40))
