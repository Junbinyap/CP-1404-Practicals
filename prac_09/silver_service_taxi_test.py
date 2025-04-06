from prac_09.silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print(fancy_taxi)
    print(f"Fare for 18km: ${fare}")


test_silver_service_taxi()
