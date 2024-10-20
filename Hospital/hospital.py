from patient import Patient
from doctor import Doctor
from nurse import Nurse
class Hospital:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.appointments = []
        self.persons = []

    def add_person(self, person):
        """Adds a person (Doctor, Nurse, Patient) to the hospital's persons list"""
        self.persons.append(person)

    def get_persons_by_type(self, person_type):
        """Returns a list of persons based on their type (Patient, Doctor, Nurse)"""
        return [person for person in self.persons if isinstance(person, person_type)]

    def add_appointment(self, appointment):
        """Adds an appointment to the hospital"""
        self.appointments.append(appointment)

    def get_appointments(self):
        """Returns the list of all appointments"""
        return self.appointments

    def display_person_details(self, person_type):
        """Displays details of persons (Doctor, Nurse, Patient) based on the type"""
        persons = self.get_persons_by_type(person_type)
        if not persons:
            print(f"No {person_type.__name__.lower()}s found.")
        for person in persons:
            print(f"{person_type.__name__}: {person.get_name()}, Age: {person.get_age()}")

    def is_doctor_available(self, doctor, appointment_date):
        """Checks if the doctor is available on a given date"""
        for appointment in self.appointments:
            if appointment.doctor == doctor and appointment.date == appointment_date:
                return False
        return True
    
    def get_hospital_details(self):
        patient_count = len(self.get_persons_by_type(Patient))
        doctor_count = len(self.get_persons_by_type(Doctor))
        nurse_count = len(self.get_persons_by_type(Nurse))
        appointment_count = len(self.appointments)
        
        details = (
            f"Hospital Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Total Patients: {patient_count}\n"
            f"Total Doctors: {doctor_count}\n"
            f"Total Nurses: {nurse_count}\n"
            f"Total Appointments: {appointment_count}"
        )
        return details
