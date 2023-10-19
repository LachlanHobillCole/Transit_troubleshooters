# Define the Emissions class
class Emissions:
    def __init__(self):
        self.bus_emissions = []

    def get_emissions(self, bus_id):
        # Retrieve emissions data for a specific bus
        for emissions in self.bus_emissions:
            if emissions["bus_id"] == bus_id:
                return emissions


# Define the RouteEmissions class
class RouteEmissions:
    def __init__(self):
        self.route_emissions = []

    def calculate_emissions(self, bus_data, emissions_data):
        # Implement emissions calculation logic
        calculated_emissions = (
            bus_data["route_distance"] * emissions_data["emissions_per_Kilometer"]
        )
        return calculated_emissions

    def aggregate_emissions(self, route_data):
        # Implement emissions aggregation logic
        aggregated_emissions = sum(route_data["emissions"])
        return aggregated_emissions

    # Define the Emissions class


class Emission_Factor:
    def __init__(self):
        self.emission_factor = {"CNG": 1974.1, "Diesel": 2671.2}

    def get_emission_factor(self, fuel_type):
        # Retrieve emissions data for a specific bus
        if fuel_type in self.emission_factor:
            return self.emission_factor.get(fuel_type)
        else:
            return None
