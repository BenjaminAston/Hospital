from patient import Patient
from doctor import Doctor

class Appointment:
    def __init__(self, doctor, patient, time: str):
        self.doctor = doctor
        self.patient = patient
        self.time = time

    def get_appointment_details(self) -> str:
        return f"Appointment: {self.patient.get_name()} with Dr. {self.doctor.get_name()} at {self.time}"