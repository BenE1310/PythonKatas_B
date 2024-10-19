class Car:
    """
    Represents a car in a car rental system.
    Attributes:
    - model: The model of the car (e.g., Toyota, Honda).
    - year: The manufacturing year of the car.
    - rented: A boolean flag indicating whether the car is currently rented.

    Methods:
    - rent_car(): Marks the car as rented.
    - return_car(): Marks the car as returned if it was rented, otherwise raises a RuntimeError.
    - is_rented(): Returns True if the car is currently rented, False otherwise.
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.rented = False  # Initial state of the car is not rented

    def rent_car(self):
        self.rented = True  # Car is now rented

    def return_car(self):
        if not self.rented:
            raise RuntimeError("Car is not rented")
        self.rented = False  # Car is now returned

    def is_rented(self):
        return self.rented  # Returns the rental status of the car


if __name__ == "__main__":
    my_car = Car("Toyota", 2010)

    print(my_car.model)  # Toyota
    print(my_car.year)  # 2010
    print(my_car.is_rented())  # False

    try:
        my_car.return_car()  # Try to return a car that isn't rented
        print('Car returned')
    except RuntimeError as e:
        print(e)  # Car is not rented

    my_car.rent_car()  # Rent the car

    print(my_car.is_rented())  # True

    my_car.return_car()  # Return the car
    print("Car returned successfully")
