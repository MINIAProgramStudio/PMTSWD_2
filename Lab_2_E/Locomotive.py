from LocoParts import *
import sys

class Locomotive:
    def __init__(self, owner: str, name: str):
        if not isinstance(owner,str):
            sys.stderr.write("ERR: owner must be str")
            exit(-1)
        if not isinstance(name,str):
            sys.stderr.write("ERR: name must be str")
            exit(-1)
        self.owner = owner
        self.name = name

    def set_engine(self, engine: Engine):
        if not isinstance(engine, Engine):
            sys.stderr.write("ERR: engine must be Engine")
            exit(-1)
        self.engine = engine

    def set_transmission(self, transmission: Transmission):
        if not isinstance(transmission, Transmission):
            sys.stderr.write("ERR: transmission must be Transmission")
            exit(-1)
        self.transmission = transmission

    def set_wheels(self, wheels: Wheels):
        if not isinstance(wheels, Wheels):
            sys.stderr.write("ERR: wheels must be Wheels")
            exit(-1)
        self.wheels = wheels

    def set_cab(self, cab: Cab):
        if not isinstance(cab, Cab):
            sys.stderr.write("ERR: cab must be Cab")
            exit(-1)
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
    has {int(self.get_axel_load())}Kg axel load"""
