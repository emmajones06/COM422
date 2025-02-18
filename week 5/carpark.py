class carpark:

    def __init__(self, capacity):
        self.spaces = []
        self.capacity = capacity

    def add_car(self, car):
        if len(self.spaces) < self.capacity and car.kind = "Car" and not self.is_duplicate(car):
            self.spaces.append(car)
            return True
        return False

    def is_duplicate(self, reg_num):
        for car in self.spaces:
            if car.reg == reg_num:
                return True
        return False

    def remove_car(self, car):
        self.spaces.remove(car)

    def spaces_left(self):
        return self.capacity - len(self.spaces)