from abc import ABC, abstractmethod

class Abstractdetails(ABC):
    def __init__(self, bank, num_pin,password):
        self.bank = bank 
        self.num_pin = num_pin
        self.password = password

    @abstractmethod
    def display_details(self):
        pass