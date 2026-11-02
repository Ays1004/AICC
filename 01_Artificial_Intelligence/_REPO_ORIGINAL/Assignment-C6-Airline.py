# Assignment-C6 (Expert System - Airline Scheduling and Cargo Schedules)

"""
THIS CODE HAS BEEN TESTED AND IS FULLY OPERATIONAL.

Problem Statement: Implement any one of the following Expert System
  VI. Airline scheduling and cargo schedules

Code from ArtificialIntelligence (SPPU - Third Year - Computer Engineering - Content) repository on KSKA Git: https://git.kska.io/sppu-te-comp-content/ArtificialIntelligence
"""

"""
Install required package: experta
pip install experta
"""

# BEGINNING OF CODE
from experta import *

class Flight(Fact):
    """Flight details"""
    flight_id: str
    aircraft_type: str
    available: bool
    pilot_available: bool
    destination: str

class Cargo(Fact):
    """Cargo details"""
    cargo_id: str
    weight: float
    category: str  # e.g., perishable, fragile, standard
    priority: str  # high, medium, low
    destination: str

# Define the Expert System
class AirlineExpertSystem(KnowledgeEngine):

    @Rule(Cargo(weight=P(lambda x: x > 10000)))
    def reject_heavy_cargo(self):
        print("Cargo rejected: Weight exceeds limit (10,000kg).")

    @Rule(
        Flight(available=True, pilot_available=True, destination=MATCH.dest),
        Cargo(destination=MATCH.dest, priority='high')
    )
    def schedule_high_priority(self, dest):
        print(f"High priority cargo scheduled to {dest} on available flight.")

    @Rule(
        Flight(available=True, pilot_available=True, destination=MATCH.dest),
        Cargo(destination=MATCH.dest, category='perishable')
    )
    def schedule_perishable(self, dest):
        print(f"Perishable cargo assigned to next available flight to {dest}.")

    @Rule(
        Flight(available=True, pilot_available=True, destination=MATCH.dest),
        Cargo(destination=MATCH.dest)
    )
    def schedule_standard(self, dest):
        print(f"Standard cargo scheduled to {dest}.")

    @Rule(Flight(available=False))
    def no_flight(self):
        print("No flight available currently.")

    @Rule(Flight(pilot_available=False))
    def no_pilot(self):
        print("No pilot available for the flight.")

# Function to get user input and run the system
def run_system():
    engine = AirlineExpertSystem()
    engine.reset()

    print("\nEnter Flight Details")
    flight_id = input("Flight ID: ")
    aircraft_type = input("Aircraft Type: ")
    available = input("Is Flight Available? (yes/no): ").lower() == 'yes'
    pilot_available = input("Is Pilot Available? (yes/no): ").lower() == 'yes'
    destination = input("Destination: ")

    flight_fact = Flight(
        flight_id=flight_id,
        aircraft_type=aircraft_type,
        available=available,
        pilot_available=pilot_available,
        destination=destination
    )
    print(f"Declaring Flight Fact: {flight_fact}")
    engine.declare(flight_fact)

    print("\nEnter Cargo Details")
    cargo_id = input("Cargo ID: ")
    
    # Input validation for weight
    while True:
        try:
            weight = float(input("Weight (in kg): "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(e)

    category = input("Category (perishable/fragile/standard): ").lower()
    priority = input("Priority (high/medium/low): ").lower()
    cargo_destination = input("Destination: ")

    cargo_fact = Cargo(
        cargo_id=cargo_id,
        weight=weight,
        category=category,
        priority=priority,
        destination=cargo_destination
    )
    print(f"Declaring Cargo Fact: {cargo_fact}")
    engine.declare(cargo_fact)

    print("\nRunning Expert System...\n")
    try:
        engine.run()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_system()
# END OF CODE
