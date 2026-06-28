# Задание 2. Класс Черепашка
import math

class Cherepashka:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        # ТЗ написано с опечаткой ("увеличивает y на s" — логически это go_right = +x)
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s - 1 <= 0:
            raise ValueError("Шаг s не может быть <= 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        """Минимальное количество ходов от текущей позиции до (x2, y2).
        За один ход черепашка смещается на s клеток по одной оси.
        Используем ceil-деление, так как последний ход может быть неполным только
        концептуально, но черепашка всегда делает ровно s клеток за ход.
        Правильная формула: ceil(|dx|/s) + ceil(|dy|/s).
        """
        dx = abs(x2 - self.x)
        dy = abs(y2 - self.y)
        return math.ceil(dx / self.s) + math.ceil(dy / self.s)


# --- Демонстрация ---
if __name__ == "__main__":
    t = Cherepashka(x=0, y=0, s=2)
    print(f"Старт: x={t.x}, y={t.y}, s={t.s}")

    t.go_right()
    t.go_up()
    print(f"После go_right + go_up: x={t.x}, y={t.y}")

    moves = t.count_moves(10, 10)
    print(f"Ходов до (10,10): {moves}")

    t.evolve()
    print(f"После evolve: s={t.s}")

    t.degrade()
    print(f"После degrade: s={t.s}")
