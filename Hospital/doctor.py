# doctor.py
from person import Person

class Doctor(Person):
    def __init__(self, name: str, age: int, role: str = "Doctor"):
        super().__init__(name, age, role)

    def perform_task(self):
        print(f"{self.name} is diagnosing.")
