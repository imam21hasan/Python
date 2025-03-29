class Magic:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Magic str value : {self.value}"

    def __repr__(self):
        return f"Magic repr value : {self.value}"

    def __add__(self, other):
        if isinstance(other, Magic):
            return Magic(self.value + other.value)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Magic(self.value * other)
        return NotImplemented

    def __eq__(self, other):
        return self.value == other.value if isinstance(other, Magic) else False

    def __len__(self):
        return abs(self.value)


a = Magic(10)
b = Magic(20)

print(a)
print(repr(a))

c = a + b
print(c)

d = a * 5
print(d)

print(a == b)
print(len(a))
