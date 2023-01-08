

# 차량 1
car_company_1 = "Ferrari"
car_detail_1 = [
    {"color": "white"},
    {"horsepower": 400},
    {"price": 8000}
]

# 차량 2
car_company_2 = "Bmw"
car_detail_2 = [
    {"color": "black"},
    {"horsepower": 270},
    {"price": 5000}
]

# 차량 3
car_company_3 = "Audi"
car_detail_3 = [
    {"color": "Silver"},
    {"horsepower": 300},
    {"price": 6000}
]

# 리스트 구조
car_company_list = ["Ferrari", "Bmw", "Audi"]
car_detail_list = [
    {"color": "white", "horsepower": 400, "price": 8000},
    {"color": "black", "horsepower": 270, "price": 5000},
    {"color": "Silver", "horsepower": 300, "price": 6000},
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()

car_dict = [
    {"car_company": "Ferrari", "car_detail": {"color": "white", "horsepower": 400, "price": 8000}},
    {"car_company": "Bmw", "car_detail": {"color": "black", "horsepower": 270, "price": 5000}},
    {"car_company": "Audi", "car_detail": {"color": "Silver", "horsepower": 300, "price": 6000}}
]

print(car_dict)
print()
print()


class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)
print(dir(car1))


print()
print()

car_list = [car1, car2, car3]

print(car_list)

for i in car_list:
    print(i)  # __str__
    print(repr(i))  # __repr__


