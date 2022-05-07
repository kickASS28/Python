class Descriptor:
    def __init__(self, value=1):
        try:
            value = float(value)
            self.value = round(abs(value))
        except ValueError:
            raise ValueError(f"invalid literal for PositiveInt() with base 10: {value}")

    def __get__(self, instance, owner):
        return instance.__dict__[self.value]

    def __set__(self, instance, value):
        try:
            value = float(value)
            instance.__dict__[self.value] = round(abs(value))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {value}")

    def __delete__(self, instance):
        del instance.__dict__[self.value]

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __add__(self, other):
        if isinstance(other, PositiveInt):
            return PositiveInt(self.value + other.value)
        try:
            other = float(other)
            return PositiveInt(self.value + round(abs(other)))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")

    def __sub__(self, other):
        try:
            if isinstance(other, PositiveInt):
                return PositiveInt(self.value - other.value)
            other = float(other)
            return PositiveInt(abs(self.value - round(abs(other))))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")

    def __mul__(self, other):
        if isinstance(other, PositiveInt):
            return PositiveInt(self.value * other.value)
        try:
            other = float(other)
            return PositiveInt(round(self.value * round(abs(other))))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")

    def __truediv__(self, other):
        if isinstance(other, PositiveInt):
            return PositiveInt(self.value // other.value)
        try:
            other = float(other)
            return PositiveInt(self.value / round(abs(other)))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")
            


class PositiveInt(Descriptor):
    value = Descriptor()


if __name__ == "__main__":
    sep = "#" * 70
    P1 = PositiveInt(50)
    P2 = PositiveInt(-20)
    P3 = PositiveInt(16.5)
    print(sep)
    print(f"PositiveInt of 50 is {P1}\nPositiveInt of -20 is {P2}\nPositiveInt of 16.5 is {P3}")
    print(sep)
    ans = P1 * 20.5
    ans2 = P2 / 10
    ans3 = P3 - 10
    ans4 = P3 + P2
    print(sep)
    print("Any number Multiplied PositiveInt is PositiveInt")
    print(f"PositiveInt 50 * Float 20.5 = PositiveInt {ans}")
    print(sep)
    print("PositiveInt Devided by any number is PositiveInt")
    print(f"PositiveInt 20 / Int 10 = PositiveInt {ans2}")
    print(sep)
    print("Addition and Substrction will return PositiveInt")
    print(f"PostiveInt {P3} - Int 10 = PositiveInt {ans3}")
    print(f"PostiveInt {P3} + PostiveInt {P2} = PositiveInt {ans4}")
    print(sep)
