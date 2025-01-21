class Car:
    def __init__(self, make, model, year, currentSpeed, maxSpeed, fuelLevel):
        self.make = make
        self.model = model
        self.year = year
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel

    def accelerate(self):
        self.currentSpeed += self.currentSpeed
        self.fuelLevel -= self.fuelLevel

    def brake(self):
        self.currentSpeed -= self.currentSpeed

    def refuel(self):
        self.fuelLevel += 1