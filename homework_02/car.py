"""
create class `Car` the child class of class `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine: Engine

    def set_engine(self, new_value_value: Engine):
        self.engine = new_value_value
