from patient import Patient
from doctor import Doctor
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
            print("Choose an option")
            print("1. Add patient to the hospital")
            print("2. Add doctor to the hospital")
            print("3. Book appointment")
            print("4. Display doctor details")
            print("5. Display patient details") 
            user_choise = input("Your choice: ")
            print()

            if user_choise == "1":
                print()
                self.add_patient()
                
            elif user_choise == "2":
                print()
                self.add_doctor()
            
            elif user_choise == "3":
                print()
                self.book_appointment()

            elif user_choise == "4":
                print()
                self.display_doctor_details()

            elif user_choise == "5":
                print()
                self.display_patient_details()

            else:
                print("The alternative doesn't exist, try again")
                print()

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
        pass  # Implement patient addition logic here

    def add_doctor(self):
        pass  # Implement doctor addition logic here

    def book_appointment(self):
        pass

    def display_doctor_details(self):
        pass  # Implement doctor details display logic here

    def display_patient_details(self):
        pass  # Implement patient details display logic here

if __name__ == "__main__":
    menu = Hospital(name="Greendale Hospital", address="Bokskogsvägen 45")
    menu.menu()