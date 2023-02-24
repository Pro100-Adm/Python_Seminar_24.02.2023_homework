class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Not negative!")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road():
    _length = NonNegative()
    _width = NonNegative()
    _mass = NonNegative()
    _thickness = NonNegative()

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._mass = 50
        self._thickness = 0.1

    def calc_mass(self):
        mass = self._length * self._width * self._mass * self._thickness
        if mass >= 1000:
            return f"Road mass = {mass / 1000} t."
        return f"Road mass = {mass} kg."


new_road = Road(500, 30)
print(new_road.calc_mass())

new_road2 = Road(10, -10)
print(new_road2.calc_mass())
