from prac_09.unreliable_car import UnreliableCar

def main():
    good_car = UnreliableCar("Good", 100, 80)
    bad_car = UnreliableCar("Bad", 100, 10)

    for i in range(1, 10):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name:5} drove {good_car.drive(i):1}km")
        print(f"{bad_car.name:5} drove {bad_car.drive(i):1}km")

    print(good_car)
    print(bad_car)


main()