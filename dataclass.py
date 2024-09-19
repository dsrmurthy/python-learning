''' PythonApp: Demo on Data classes by DSR Murthy'''
from dataclasses import dataclass

@dataclass
class Car:
    color: str
    mileage: float
    automatic: bool

if __name__=='__main__':
    car1 = Car("red", 3812.4, True)
    print(car1)
    print(f"car mileage{car1.mileage}")
