class Engine:
    def __init__(self, power: int, fuel_consumption: int, mass: int):
        self.power = power
        self.fuel_consumption = fuel_consumption
        self.mass = mass

    def __str__(self) -> str:
        return f"{self.power}W engine that consumes {self.fuel_consumption}L/h and weighs {self.mass}Kg"


class Transmission:
    def __init__(self, resistance_force, mass):
        self.resistance_force = resistance_force
        self.mass = mass

    def __str__(self) -> str:
        return f"transmission with a {self.resistance_force}N resistance and that weighs {self.mass}Kg"


class Wheels:
    def __init__(self, axels_count, radius, mass):
        self.axels_count = axels_count
        self.radius = radius
        self.mass = mass

    def __str__(self) -> str:
        return f"wheels are located on {self.axels_count} axels, have {self.radius}mm radius and weigh {self.mass}Kg"


class Cab:
    def __init__(self, colour, mass):
        self.colour = colour
        self.mass = mass

    def __str__(self) -> str:
        return f"cab is painted in {self.colour} and weighs {self.mass}Kg"
