from patient import Patient
from doctor import Doctor
from nurse import Nurse
from appointment import Appointment

class Hospital:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.appointments = []
        self.persons = []

    def menu(self):
        while True:

            print()
            print("Choose an option:")
            print("1. Add patient to the hospital")
            print("2. Add doctor to the hospital")
            print("3. Add nurse to the hospital")
            print("4. Book appointment")
            print("5. Display doctor details")
            print("6. Display patient details")
            print("7. Display nurse details")
            print("8. Display all appointments")
            user_choice = input("Your choice: ")
            print()

            if user_choice == "1":
                self.add_patient()

            elif user_choice == "2":
                self.add_doctor()

            elif user_choice == "3":
                self.add_nurse()

            elif user_choice == "4":
                self.book_appointment()

            elif user_choice == "5":
                self.display_doctor_details()

            elif user_choice == "6":
                self.display_patient_details()

            elif user_choice == "7":
                self.display_nurse_details()

            elif user_choice == "8":
                self.display_all_appointments()

            else:
                print("Invalid option. Please try again.")

    def validate_non_empty_string(self, prompt: str) -> str:
        """A try and except function that makes sure the use puts in the right values"""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty. Please try again.")

    def validate_positive_integer(self, prompt: str) -> int:
        """A try and except function that makes sure that the user puts in a positive integer"""
        while True:
            value = input(prompt).strip()
            if value.isdigit() and int(value) > 0:
                return int(value)
            print("Invalid input. Please enter a positive integer.")

    def validate_positive_float(self, prompt: str) -> float:
        """A try and except function that makes sure the user puts in a positive number"""
        while True:
            value = input(prompt).strip()
            try:
                value = float(value)
                if value > 0:
                    return value
            except ValueError:
                pass
            print("Invalid input. Please enter a positive number.")

    def add_patient(self):
        name = self.validate_non_empty_string("Enter patient's name: ")
        age = self.validate_positive_integer("Enter patient's age: ")
        new_patient = Patient(name=name, age=age)
        self.add_person(new_patient)
        print(f"Patient {new_patient.get_name()} added successfully!")

    def add_person(self, person):
        """Adds a person (Doctor, Nurse, Patient) to the hospital's persons list"""
        self.persons.append(person)

    def add_doctor(self):
        name = self.validate_non_empty_string("Enter doctor name: ")
        age = self.validate_positive_integer("Enter doctor age: ")
        new_doctor = Doctor(name, age)
        self.add_person(new_doctor)
        print(f"Doctor {new_doctor.get_name()} added successfully.")

    def add_nurse(self):
        name = self.validate_non_empty_string("Enter nurse name: ")
        age = self.validate_positive_integer("Enter nurse age: ")
        new_nurse = Nurse(name, age)
        self.add_person(new_nurse)
        print(f"Nurse {new_nurse.get_name()} added successfully.")

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)

    def book_appointment(self):
        # Filter patients and doctors from persons list
        patients = [person for person in self.persons if isinstance(person, Patient)]
        doctors = [person for person in self.persons if isinstance(person, Doctor)]

        if not patients:
            print("No patients available for appointments.")
            return

        if not doctors:
            print("No doctors available for appointments.")
            return

        # Display available patients
        print("Available Patients:")
        for idx, patient in enumerate(patients, 1):
            print(f"{idx}. {patient.get_name()} (Age: {patient.get_age()})")

        patient_choice = self.validate_positive_integer("Select a patient by number: ") - 1
        if patient_choice < 0 or patient_choice >= len(patients):
            print("Invalid patient selection.")
            return
        selected_patient = patients[patient_choice]

        # Display available doctors
        print("Available Doctors:")
        for idx, doctor in enumerate(doctors, 1):
            print(f"{idx}. Dr. {doctor.get_name()}")

        doctor_choice = self.validate_positive_integer("Select a doctor by number: ") - 1
        if doctor_choice < 0 or doctor_choice >= len(doctors):
            print("Invalid doctor selection.")
            return
        selected_doctor = doctors[doctor_choice]

        # Get the appointment date
        appointment_date = self.validate_non_empty_string("Enter appointment date (YYYYMMDD): ")

        # Check if the doctor is already booked on that date
        for appointment in self.appointments:
            if appointment.doctor == selected_doctor and appointment.date == appointment_date:
                print(f"Doctor {selected_doctor.get_name()} is already booked on {appointment_date}. Please choose another date or doctor.")
                self.book_appointment()

        # Book the appointment (doctor first, then patient)
        new_appointment = Appointment(selected_doctor, selected_patient, appointment_date)
        self.add_appointment(new_appointment)
        print(f"Appointment booked: {new_appointment}")




    def display_doctor_details(self):
        for person in self.persons:
            if isinstance(person, Doctor):
                print(f"Doctor: {person.get_name()}, Age: {person.get_age()}")


    def display_patient_details(self):
        for person in self.persons:
            if isinstance(person, Patient):
                print(f"Patient: {person.get_name()}, Age: {person.get_age()}")
    
    def display_nurse_details(self):
        for person in self.persons:
            if isinstance(person, Nurse):
                print(f"Nurse: {person.get_name()}, Age: {person.get_age()}")

    def display_all_appointments(self):
        if not self.appointments:
            print("No appointments scheduled.")
        else:
            for appointment in self.appointments:
                print(appointment)

if __name__ == "__main__":
    menu = Hospital(name="Greendale Hospital", address="Bokskogsvägen 45")
    menu.menu()