from patient import Patient
from doctor import Doctor
from nurse import Nurse
from appointment import Appointment
from hospital import Hospital

class Menu:
    def __init__(self, hospital: Hospital):
        self.hospital = hospital

    def menu(self):
        """Menu that lets the user control the outcome of the program."""
        while True:
            print()
            print("Choose an option:")
            print("1. Add patient to the hospital")
            print("2. Add doctor to the hospital")
            print("3. Add nurse to the hospital")
            print("4. Book appointment")
            print("5. Display patient details")
            print("6. Display doctor details")
            print("7. Display nurse details")
            print("8. Display all appointments")
            print("9. Display hospital details")
            print("10. Perform task")
            user_choice = input("Your choice: ").strip()

            if user_choice == "1":
                print()
                self.add_person(Patient, "patient")
            elif user_choice == "2":
                print()
                self.add_person(Doctor, "doctor")
            elif user_choice == "3":
                print()
                self.add_person(Nurse, "nurse")
            elif user_choice == "4":
                print()
                self.book_appointment()
            elif user_choice == "5":
                print()
                self.hospital.display_person_details(Patient)
            elif user_choice == "6":
                print()
                self.hospital.display_person_details(Doctor)
            elif user_choice == "7":
                print()
                self.hospital.display_person_details(Nurse)
            elif user_choice == "8":
                print()
                self.display_all_appointments()
            elif user_choice == "9":
                print()
                self.display_hospital_details()
            elif user_choice == '10':
                print()
                self.perform_task()
            else:
                print("Invalid option. Please try again.")

    def add_person(self, person_class, role: str):
        """Adds a new person (patient, doctor, nurse) to the hospital."""
        name = self.validate_non_empty_string(f"Enter {role}'s name: ")
        age = self.validate_positive_integer(f"Enter {role}'s age: ")
        new_person = person_class(name, age)
        self.hospital.add_person(new_person)
        print()
        print(f"{role.capitalize()} {new_person.get_name()} added successfully!")

    def book_appointment(self):
        """""Function that makes it possible for the user to book an appointment for a patient with a doctor."""
        patients = self.hospital.get_persons_by_type(Patient)
        doctors = self.hospital.get_persons_by_type(Doctor)

        if not patients:
            print("No patients available for appointments.")
            return

        if not doctors:
            print("No doctors available for appointments.")
            return

        print("Available Patients:")
        for idx, patient in enumerate(patients, 1):
            print(f"{idx}. {patient.get_name()} (Age: {patient.get_age()})")

        patient_choice = self.validate_positive_integer("Select a patient by number: ") - 1
        if patient_choice < 0 or patient_choice >= len(patients):
            print("Invalid patient selection.")
            return
        selected_patient = patients[patient_choice]

        print("Available Doctors:")
        for idx, doctor in enumerate(doctors, 1):
            print(f"{idx}. Dr. {doctor.get_name()}")

        doctor_choice = self.validate_positive_integer("Select a doctor by number: ") - 1
        if doctor_choice < 0 or doctor_choice >= len(doctors):
            print("Invalid doctor selection.")
            return
        selected_doctor = doctors[doctor_choice]

        appointment_date = self.validate_non_empty_string("Enter appointment date (YYYYMMDD): ")

        if not self.hospital.is_doctor_available(selected_doctor, appointment_date):
            print(f"Doctor {selected_doctor.get_name()} is already booked on {appointment_date}. Please choose another date or doctor.")
            return
    
        appointment_name = self.validate_non_empty_string("Enter appointment name: ")

        new_appointment = Appointment(selected_doctor, selected_patient, appointment_date, appointment_name)
        self.hospital.add_appointment(new_appointment)
        print()
        print(f"Appointment booked: {new_appointment}")

    def display_all_appointments(self):
        """""Function that displays a booked appointment"""
        appointments = self.hospital.get_appointments()
        if not appointments:
            print("No appointments scheduled.")
        else:
            for appointment in appointments:
                print(appointment)

    def display_hospital_details(self):
        """Displays the details of the hospital."""
        details = self.hospital.get_hospital_details()
        print(details)
    
    def perform_task(self):
        """Lets the user pick a person in a specific role to preform a tailored task"""
        print("Pick a role:")
        print("1. Patient")
        print("2. Doctor")
        print("3. Nurse")
        role_choice = input("Your choice: ")

        if role_choice == "1":
            persons = self.hospital.get_persons_by_type(Patient)
            role = "patient"
        elif role_choice == "2":
            persons = self.hospital.get_persons_by_type(Doctor)
            role = "doctor"
        elif role_choice == "3":
            persons = self.hospital.get_persons_by_type(Nurse)
            role = "nurse"
        else:
            print("Invalid role selection.")
            return

        if not persons:
            print(f"No {role}s available.")
            return

        print(f"Available {role.capitalize()}s:")
        for idx, person in enumerate(persons, 1):
            print(f"{idx}. {person.get_name()} (Age: {person.get_age()})")

        person_choice = self.validate_positive_integer(f"Select a {role} by number: ") - 1

        if person_choice < 0 or person_choice >= len(persons):
            print(f"Invalid {role} selection.")
            return

        selected_person = persons[person_choice]
        print()
        selected_person.perform_task()
        
    def validate_non_empty_string(self, prompt: str) -> str:
        """Prompts the user for input and ensures the input is a non-empty string"""
        while True:
            value = input(prompt).strip()
            if value and all(x.isalpha() or x.isspace() for x in value):
                return value
            print("Input must be string Please try again.")

    def validate_positive_integer(self, prompt: str) -> int:
        """Prompts the user for input and ensures the input is a positive integer."""
        while True:
            value = input(prompt).strip()
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    hospital = Hospital(name="Greendale Hospital", address="Bokskogsvägen 45")

    patients = [
        Patient(name="John", age=30),
        Patient(name="Jane", age=25),
        Patient(name="Mike", age=40),
        Patient(name="Emily", age=35),
        Patient(name="Robert", age=28)
    ]
    
    doctors = [
        Doctor(name="Alice", age=45),
        Doctor(name="James", age=50),
        Doctor(name="Emma", age=38),
        Doctor(name="Michael", age=42),
        Doctor(name="Olivia", age=47)
    ]
    
    nurses = [
        Nurse(name="Sarah", age=32),
        Nurse(name="David", age=29),
        Nurse(name="Lisa", age=37),
        Nurse(name="Daniel", age=31),
        Nurse(name="Clark", age=36)
    ]

    for patient in patients:
        hospital.add_person(patient)
    
    for doctor in doctors:
        hospital.add_person(doctor)
    
    for nurse in nurses:
        hospital.add_person(nurse)

    menu = Menu(hospital)
    menu.menu()
