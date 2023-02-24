class MyMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Road(metaclass=MyMeta):
    _mass = 50
    _thickness = 0.1

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * self._mass * self._thickness
        if mass >= 1000:
            return f"Road mass = {mass / 1000} t."
        return f"Road mass = {mass} kg."


new_road = Road(500, 30)
print(new_road.calc_mass())

new_road2 = Road(10, -10)
print(new_road2.calc_mass())

print(new_road is new_road2)