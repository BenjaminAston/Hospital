from patient import Patient
from doctor import Doctor


class Appointment:
    next_id = 1
    def __init__(self, doctor, patient, date, appointment_name):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.appointment_id = Appointment.next_id
        Appointment.next_id += 1
        self.appointment_name = appointment_name

    def __str__(self):
        return (f"Appointment ID: {self.appointment_id}, Appointment Name: {self.appointment_name}, "
                f"Patient: {self.patient.get_name()}, Doctor: Dr. {self.doctor.get_name()}, Date: {self.date}")
