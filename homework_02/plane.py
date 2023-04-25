"""
create class `Plane` the child class of class `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo: int = 0
    max_cargo:int = 100

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
    
    def load_cargo(self, new_cargo: int):
        final_cargo = self.cargo + new_cargo

        if final_cargo <= self.max_cargo:
            self.cargo = final_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
