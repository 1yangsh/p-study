class Car:
    """
    Car class
    author : Yang
    Date : 2022.01.07
    Detail : Class, Static, instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    # instance method
    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    def get_price(self):
        return f'Before car price: company -> {self._company}, price -> {self._details.get("price")}'

    def get_price_calc(self):
        return f'After car price: company -> {self._company}, price -> {self._details.get("price") * Car.price_per_raise}'

    # class method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print("Succeed! price increased.")

    # static method
    @staticmethod
    def is_bmw(inst):
        if inst._company == "Bmw":
            return f"OK! This car is {inst._company}."
        return "Sorry. This car is not Bmw."

    def __str__(self):
        return f"str : {self._company} - {self._details}"

    def __repr__(self):
        return f"repr : {self._company} - {self._details}"


car1 = Car("Ferrari", {"color": "white", "horsepower": 400, "price": 8000})
car2 = Car("Bmw", {"color": "black", "horsepower": 270, "price": 5000})
car3 = Car("Audi", {"color": "Silver", "horsepower": 300, "price": 6000})

print(car1._details.get("price"))


# 가격 인상 전
print(car1.get_price())

Car.price_per_raise = 1.4  # 클래스 메소드 직접 접근 (권장X)
# 가격 인상 후
print(car1.get_price_calc())

# 클래스 메소드 사용
Car.raise_price(0.9)
Car.raise_price(1.6)

# 가격 인상 후
print(car1.get_price_calc())

# static method 호출
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
