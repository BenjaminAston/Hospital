from person import Person

class Patient(Person):
    def __init__(self, name: str, age: int, role: str = "Patient"):
        super().__init__(name, age, role)

    def perform_task(self):
        print(f"{self.name} is undergoing treatment.")