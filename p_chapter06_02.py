# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여러 일을 동시에 수행 -> 단일 프로그램 안에서 여러 일을 쉽게 해결
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행 -> 속도

# Generator Ex1


def generator_ex1():
    print("Start")
    yield "A Point"
    print("Continue")
    yield "B Point"
    print("End")


temp = iter(generator_ex1())
# temp = generator_ex1()

# print(temp)
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    print(v)


# Generator Ex2

temp2 = [x * 3 for x in generator_ex1()]
temp3 = (x * 3 for x in generator_ex1())

print(temp2)
print(temp3)

for i in temp2:
    print(i)

for i in temp3:
    print(i)

print()
print()


# Generator Ex3(중요 함수)
# count, takewhile, filterfalse, accumulate, chain, product, groupby, ...

import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))  # 1
print(next(gen1))  # 3.5
print(next(gen1))  # 6.0
print(next(gen1))
print(next(gen1))
# ... 무한

# 조건
gen2 = itertools.takewhile(lambda n: n < 1000, itertools.count(1, 2.5))

for v in gen2:
    pass
    # print(v)

print()
print()


# 필터 반대
gen3 = itertools.filterfalse(lambda n: n < 3, [1, 2, 3, 4, 5])

for v in gen3:
    print(v)  # 3,4,5


# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 10)])

for v in gen4:
    print(v)


# 연결1
gen5 = itertools.chain("ABCDE", range(1, 11, 2))

print(list(gen5))

# 연결2
gen6 = itertools.chain(enumerate("ABCDE"))

print(list(gen6))


# 개별
gen7 = itertools.product("ABCDE")

print(list(gen7))


# 연산(경우의 수)
gen8 = itertools.product("ABCDE", repeat=3)

print(list(gen8))


# 그룹화
gen9 = itertools.groupby("AAABBBBBCCCCCCCDDEEE")

# print(list(gen9))

for chr, group in gen9:
    print(chr, " : ", list(group))
