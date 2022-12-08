
from dataclasses import dataclass

@dataclass
class dish():
    count: int
    name: str
    cost: float
    weight: int

dish_1 = dish(1, "Тыквенный суп", 10, 700)
dish_2 = dish(1, "Чизкейк", 5.5, 400)

class order:
    def __init__(self):
        self.count = 0
        self.cost = 0
        self.weight = 0
        self.money = 0
        self.summa = 0
        self.order = []

    def properties(self, *args):
        self.order += list(args)
        for i in args:
            self.count += i.count
            self.cost += i.cost
            self.weight += i.weight
        return self.count, self.cost, self.weight

    def pay(self, money: float):
        self.money += money
        self.summa = self.cost - self.money
        if self.summa > 0:
            print(f"Вы должны еще {self.summa} рублей")
        else:
            print(f"Вот ваша сдача: {abs(self.summa)}")

order_1 = order()
order_1.properties(dish_1, dish_2)
print(order_1.count)
print(order_1.cost)
print(order_1.weight)
order_1.pay(10)
order_1.pay(4)