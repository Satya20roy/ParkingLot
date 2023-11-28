import random
import json


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return f"Car with license plate {self.license_plate}"

    def park(self, parking_lot, spot):
        return parking_lot.park(self, spot)


class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        self.spot_size = spot_size
        self.square_footage = square_footage
        self.total_spots = self.calculate_total_spots()
        self.available_spots = list(range(1, self.total_spots + 1))
        self.parking_map = {}

    def calculate_total_spots(self):
        spot_area = self.spot_size[0] * self.spot_size[1]
        return self.square_footage // spot_area

    def park(self, car, spot):
        if spot in self.available_spots:
            self.available_spots.remove(spot)
            self.parking_map[car.license_plate] = spot
            print(f"{car} parked successfully in spot {spot}")
            return True
        else:
            print(f"Spot {spot} is occupied. Trying another spot for {car}")
            return False

    def generate_parking_map(self):
        return self.parking_map


def main():
    parking_lot_size = 2000  # Change this value to the desired parking lot size
    cars = [Car(str(random.randint(1000000, 9999999))) for _ in range(20)]  # Change 10 to the number of cars you want
    parking_lot = ParkingLot(parking_lot_size)
    for car in cars:
        parked = False
        while not parked and parking_lot.available_spots:
            spot_to_park = random.choice(parking_lot.available_spots)
            parked = car.park(parking_lot, spot_to_park)

    # Save parking map to a JSON file
    parking_map = parking_lot.generate_parking_map()
    with open("parking_map.json", "w") as json_file:
        json.dump(parking_map, json_file)


if __name__ == "__main__":
    main()
