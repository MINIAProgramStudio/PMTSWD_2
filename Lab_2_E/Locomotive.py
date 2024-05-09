from LocoParts import *


class Locomotive:
    def __init__(self, owner: str, name: str):
        self.owner = owner
        self.name = name

    def set_engine(self, engine: Engine):
        self.engine = engine

    def set_transmission(self, transmission: Transmission):
        self.transmission = transmission

    def set_wheels(self, wheels: Wheels):
        self.wheels = wheels

    def set_cab(self, cab: Cab):
        self.cab = cab

    def get_total_mass(self) -> int:
        parts = [self.engine, self.wheels, self.transmission, self.cab]
        return sum([i.mass for i in parts])

    def get_axel_load(self) -> float:
        return self.get_total_mass() / self.wheels.axels_count

    def choochoo(self):
        print("Dear nearby humans, please, be aware of 3000 tons of steel rolling in your general direction.")

    def __str__(self):
        return f"""{self.owner}'s {self.name} locomotive that:
    weighs {self.get_total_mass()}Kg 
    has {int(self.get_axel_load())}Kg axel load
"""
