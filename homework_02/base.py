from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight: int = 100
    started: bool = False
    fuel: int = 80
    fuel_consumption: int = 2

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
            
    def move(self, distance: int):
        distance_fuel = distance * self.fuel_consumption
        if self.fuel < distance_fuel:
            raise NotEnoughFuel
        else:
            self.fuel -= distance_fuel
