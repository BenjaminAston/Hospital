from abc import ABC, abstractmethod

class Person:
    def __init__(self, name: str, age: int, role: str):
        self.name = name
        self.age = age
        self.role = role

    @abstractmethod
    def perform_task(self):
        raise NotImplementedError("Subclasses must implement this method")

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