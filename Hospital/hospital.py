from abc import ABC, abstractmethod
class Hospital:
    def __init__(self, name: str, address: str, appointments: str, persons: str):
        self.name = name
        self.address = address
        self.appointments = appointments
        self.persons = persons

    def menu(self):
        pass  # Implement menu logic here

    def add_patient(self):
        pass  # Implement patient addition logic here

    def add_doctor(self):
        pass  # Implement doctor addition logic here

    def display_doctor_details(self):
        pass  # Implement doctor details display logic here

    def display_patient_details(self):
        pass  # Implement patient details display logic here

class Appointment:
    def __init__(self, doctor, patient, time: str):
        self.doctor = doctor
        self.patient = patient
        self.time = time

    def get_appointment_details(self) -> str:
        return f"Appointment: {self.patient.get_name()} with Dr. {self.doctor.get_name()} at {self.time}"

class Person:
    def __init__(self, name: str, age: int, role: str):
        self.name = name
        self.age = age
        self.role = role

    def perform_duties(self):
        pass  # This is abstract, subclasses should override this

    def get_name(self) -> str:
        return self.name

    def get_age(self) -> int:
        return self.age

    def get_title(self) -> str:
        return self.role

    def get_details(self) -> dict:
        return {
            "name": self.name,
            "age": self.age,
            "role": self.role
        }


class Doctor(Person):
    def __init__(self, name: str, age: int, role: str = "Doctor"):
        super().__init__(name, age, role)

    def perform_duties(self):
        print(f"{self.name} is performing doctor duties.")


class Patient(Person):
    def __init__(self, name: str, age: int, role: str = "Patient"):
        super().__init__(name, age, role)

    def perform_duties(self):
        print(f"{self.name} is undergoing treatment.")
