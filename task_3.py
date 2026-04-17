import math

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")

        # Скорочуємо дріб при створенні
        common = math.gcd(numerator, denominator)
        self.num = numerator // common
        self.den = denominator // common

    def __add__(self, other: 'Fraction') -> 'Fraction':
        # Формула: a/b + c/d = (ad + bc) / bd
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other: 'Fraction') -> 'Fraction':
        # Формула: a/b - c/d = (ad - bc) / bd
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other: 'Fraction') -> 'Fraction':
        # Формула: a/b * c/d = ac / bd
        return Fraction(self.num * other.num, self.den * other.den)

    def __truediv__(self, other: 'Fraction') -> 'Fraction':
        # Формула: a/b / c/d = ad / bc
        return Fraction(self.num * other.den, self.den * other.num)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fraction):
            return False
        return self.num == other.num and self.den == other.den

    def __lt__(self, other: 'Fraction') -> bool:
        # Порівняння a/b < c/d через перехресне множення: ad < bc
        return self.num * other.den < other.num * self.den

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)

    # Перевірка додавання
    sum_res = x + y
    print(f"{x} + {y} = {sum_res}")
    assert sum_res == Fraction(3, 4)

    # Перевірка множення
    mul_res = x * y
    print(f"{x} * {y} = {mul_res}")
    assert mul_res == Fraction(1, 8)

    # Перевірка порівняння
    print(f"Чи {x} більше за {y}?: {x > y}")

    print("Перевірки пройдені")