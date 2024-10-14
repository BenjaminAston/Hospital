from person import Person

class Nurse(Person):
    def __init__(self, name: str, age: int, role: str = "Nurse"):
        super().__init__(name, age, role)

    def perform_task(self):
        print(f"{self.name} taking blood test.")