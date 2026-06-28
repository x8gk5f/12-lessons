# Задание 1. Класс Касса
class Kassa:
    def __init__(self, money=0):
        self.money = money

    def top_up(self, X):
        self.money += X
        print(f"Касса пополнена на {X}. Текущий баланс: {self.money}")

    def count_1000(self):
        thousands = self.money // 1000
        print(f"Целых тысяч в кассе: {thousands}")
        return thousands

    def take_away(self, X):
        if self.money >= X:
            self.money -= X
            print(f"Из кассы забрали {X}. Текущий баланс: {self.money}")
        else:
            raise ValueError("Недостаточно денег в кассе!")


# --- Демонстрация ---
if __name__ == "__main__":
    k = Kassa(money=5500)
    print(f"Начальный баланс: {k.money}")
    k.top_up(2000)
    k.count_1000()
    k.take_away(1500)
    k.count_1000()
    try:
        k.take_away(99999)
    except ValueError as e:
        print(f"Ошибка: {e}")

