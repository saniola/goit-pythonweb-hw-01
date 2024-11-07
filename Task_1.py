import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    def __init__(self, make, model, region_spec):
        self.make = make
        self.model = model
        self.region_spec = region_spec

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logging.info(
            f"{self.make} {self.model} ({self.region_spec} Spec): Engine started"
        )


class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info(
            f"{self.make} {self.model} ({self.region_spec} Spec): Engine started"
        )


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    ford_mustang = us_factory.create_car("Ford", "Mustang")
    ford_mustang.start_engine()

    bmw_r1200 = eu_factory.create_motorcycle("BMW", "R1200")
    bmw_r1200.start_engine()
