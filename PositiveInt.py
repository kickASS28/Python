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
        try:
            other = float(other)
            return PositiveInt(self.value + round(abs(other)))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")

    def __sub__(self, other):
        try:
            other = float(other)
            return PositiveInt(abs(self.value - round(abs(other))))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")

    def __mul__(self, other):
        try:
            other = float(other)
            return PositiveInt(round(self.value * round(abs(other))))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")

    def __truediv__(self, other):
        try:
            other = float(other)
            return PositiveInt(self.value // round(abs(other)))
        except ValueError:
            raise ValueError(f"You cannot create a positive integer with: {other}")


class PositiveInt(Descriptor):
    value = Descriptor()


if __name__ == "__main__":
    P1 = PositiveInt(50)
    print(P1)
    ans = P1 * 20
    print(ans)
    print(type(ans))