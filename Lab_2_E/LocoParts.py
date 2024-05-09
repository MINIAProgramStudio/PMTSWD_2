import sys
class Engine:
    def __init__(self, power: int, fuel_consumption: int, mass: int):
        if not isinstance(power, int):
            sys.stderr.write("ERR: power must be int")
            exit(-1)
        if power <= 0:
            sys.stderr.write("ERR: power must be positive")
            exit(-1)
        if not isinstance(fuel_consumption, int):
            sys.stderr.write("ERR: fuel_consumption must be int")
            exit(-1)
        if fuel_consumption <= 0:
            sys.stderr.write("ERR: fuel_consumption must be positive")
            exit(-1)
        if not isinstance(mass, int):
            sys.stderr.write("ERR: mass must be int")
            exit(-1)
        if mass <= 0:
            sys.stderr.write("ERR: mass must be positive")
            exit(-1)

        self.power = power
        self.fuel_consumption = fuel_consumption
        self.mass = mass

    def __str__(self) -> str:
        return f"{self.power}W engine that consumes {self.fuel_consumption}L/h and weighs {self.mass}Kg"


class Transmission:
    def __init__(self, resistance_force: float, mass: int):
        if isinstance(resistance_force, int):
            resistance_force = float(resistance_force)
            sys.stderr.write("WARN: resistance_force should be float")
        if not isinstance(resistance_force, float):
            sys.stderr.write("ERR: resistance_force must be float")
            exit(-1)

        if resistance_force < 0:
            sys.stderr.write("ERR: resistance_force must be positive or zero")
            exit(-1)
        if not isinstance(mass, int):
            sys.stderr.write("ERR: mass must be int")
            exit(-1)
        if mass <= 0:
            sys.stderr.write("ERR: mass must be positive")
            exit(-1)
        self.resistance_force = resistance_force
        self.mass = mass

    def __str__(self) -> str:
        return f"transmission with a {self.resistance_force}N resistance and that weighs {self.mass}Kg"


class Wheels:
    def __init__(self, axels_count: int, radius: int, mass: int):
        if not isinstance(axels_count, int):
            sys.stderr.write("ERR: axels_count must be int")
            exit(-1)
        if not axels_count >= 2:
            sys.stderr.write("ERR: axels_count must be greater or equal to 2")
            exit(-1)
        if not isinstance(radius, int):
            sys.stderr.write("ERR: radius must be int")
            exit(-1)
        if not radius <= 0:
            sys.stderr.write("ERR: radius must be positive")
            exit(-1)
        if not isinstance(mass, int):
            sys.stderr.write("ERR: mass must be int")
            exit(-1)
        if mass <= 0:
            sys.stderr.write("ERR: mass must be positive")
            exit(-1)
        self.axels_count = axels_count
        self.radius = radius
        self.mass = mass

    def __str__(self) -> str:
        return f"wheels are located on {self.axels_count} axels, have {self.radius}mm radius and weigh {self.mass}Kg"


class Cab:
    def __init__(self, colour: str, mass: int):
        if not isinstance(colour, str):
            sys.stderr.write("ERR: axels_count must be str")
            exit(-1)
        if not colour == "black":
            sys.stderr.write("ERR: car may be painted in any color if the color is black (c) H. Ford")
            exit(-1)
        if not isinstance(mass, int):
            sys.stderr.write("ERR: mass must be int")
            exit(-1)
        if mass <= 0:
            sys.stderr.write("ERR: mass must be positive")
            exit(-1)
        self.colour = colour
        self.mass = mass

    def __str__(self) -> str:
        return f"cab is painted in {self.colour} and weighs {self.mass}Kg"
