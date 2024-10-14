from patient import Patient
from doctor import Doctor

class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date

    def __str__(self):
        return f"Patient: {self.patient.get_name()}, Doctor: Dr. {self.doctor.get_name()}, Date: {self.date}"
