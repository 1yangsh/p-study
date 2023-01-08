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

    def detail_info(self):
        print(f"Current ID : {id(self)}")
        print(f"Car Detail Info : {self._company} {self._details.get('price')}")

    def get_price(self):
        return f'Before car price: company -> {self._company}, price -> {self._details.get("price")}'

    def get_price_calc(self):
        return f'After car price: company -> {self._company}, price -> {self._details.get("price") * Car.price_per_raise}'

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

Car.price_per_raise = 1.5
# 가격 인상 후
print(car1.get_price_calc())

