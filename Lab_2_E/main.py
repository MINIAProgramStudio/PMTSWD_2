from Locomotive import Locomotive
from LocoParts import *

x = Locomotive("UZ", "ChME-3")
x.set_engine(Engine(10 ** 5, 100, 5 * 10 ** 3))
x.set_cab(Cab("White", 10 ** 4))
x.set_wheels(Wheels(6,10**3,4*10**3))
x.set_transmission(Transmission(10**4,10**4))

print(x)
