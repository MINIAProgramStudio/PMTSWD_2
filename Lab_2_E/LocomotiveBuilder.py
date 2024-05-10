from Locomotive import Locomotive
from LocoParts import *
import copy


class EmptyLocomotiveBuilder:
    def __init__(self):
        pass

    def set_engine(self, engine: Engine):
        pass

    def set_transmission(self, transmission: Transmission):
        pass

    def set_wheels(self, wheels: Wheels):
        pass

    def set_cab(self, cab: Cab):
        pass


class LocomotiveBuilder(EmptyLocomotiveBuilder):
    def set_locomotive(self, locomotive: Locomotive):
        if not isinstance(locomotive, Locomotive):
            sys.stderr.write("ERR: locomotive must be Locomotive")
            exit(-1)
        self.locomotive = locomotive

    def set_engine(self, engine: Engine):
        self.locomotive.set_engine(engine)

    def set_transmission(self, transmission: Transmission):
        self.locomotive.set_transmission(transmission)

    def set_wheels(self, wheels: Wheels):
        self.locomotive.set_wheels(wheels)

    def set_cab(self, cab: Cab):
        self.locomotive.set_cab(cab)

    def check(self):
        if not hasattr(self, "locomotive"):
            return False
        if not hasattr(self.locomotive, "engine"):
            return False
        if not hasattr(self.locomotive, "transmission"):
            return False
        if not hasattr(self.locomotive, "wheels"):
            return False
        if not hasattr(self.locomotive, "cab"):
            return False

        if not isinstance(self.locomotive.engine, Engine):
            return False
        if not isinstance(self.locomotive.transmission, Transmission):
            return False
        if not isinstance(self.locomotive.wheels, Wheels):
            return False
        if not isinstance(self.locomotive.cab, Cab):
            return False

        return True

    def get_locomotive(self):
        if self.check():
            return copy.deepcopy(self.locomotive)
        else:
            return -1
