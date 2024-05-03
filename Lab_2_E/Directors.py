from LocomotiveBuilder import LocomotiveBuilder
from Locomotive import Locomotive
from LocoParts import *


class ChME_3:
    def __init__(self):
        pass
    def construct(self):
        builder = LocomotiveBuilder()
        builder.set_locomotive(Locomotive("УЗ", "ЧМЕ-3"))
        builder.set_engine(Engine(1012500, 100, 60 * 10 ** 3))
        builder.set_transmission(Transmission(100, 20 * 10 ** 3))
        builder.set_wheels(Wheels(6, 10 * 10 ** 3))
        return builder.get_locomotive()
