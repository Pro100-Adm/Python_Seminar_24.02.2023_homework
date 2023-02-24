class MyMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MyMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Worker(metaclass=MyMeta):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __str__(self):
        return f"Worker's full name: {self.name} {self.surname}"

    def get_full_name(self):
        return str(self)

    def get_total_income(self):
        total_income = self._income["wage"] + self._income["bonus"]
        return f"Worker's total income: {total_income}"


Employeer_1 = Position("Ivan", "Petrov", "Lab worker", 22000, 10000)
print(Employeer_1.get_full_name())
print(Employeer_1.name)
print(Employeer_1.surname)
print(Employeer_1.position)
print(Employeer_1._income)
print(Employeer_1.get_total_income())

Employeer_2 = Position("Viktor", "Sidorov", "School Headmaster", 150000, 100000)
print(Employeer_2.get_full_name())
print(Employeer_2.name)
print(Employeer_2.surname)
print(Employeer_2.position)
print(Employeer_2._income)
print(Employeer_2.get_total_income())

print(Employeer_1 is Employeer_2)
