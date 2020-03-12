class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": salary, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        fullname = self.name + " " + self.surname
        print(f"ФИО: {fullname}")

    def get_total_income(self):
        tot_inc = self._income.get("wage") + self._income.get("bonus")
        print(f"Общий доход: {tot_inc}")


my_worker = Position("Alex", "Stone", "Director", 10000, 1200)
my_worker2 = Position("Claudia", "Banks", "Manager", 5000, 500)

my_worker.get_full_name()
my_worker.get_total_income()
my_worker2.get_full_name()
my_worker2.get_total_income()