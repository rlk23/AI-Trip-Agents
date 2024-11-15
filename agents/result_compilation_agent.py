class ResultCompilationAgent:
    def format_results(self, flight_data, min_price=None, max_price=None, max_results=5):
        """
        Format and display flight results based on price range, or top `max_results` flights if no matches are found.

        Args:
            flight_data (dict): The raw flight data returned from the API.
            min_price (float): The minimum price to filter flights by.
            max_price (float): The maximum price to filter flights by.
            max_results (int): The maximum number of fallback flights to display if no matches are found.
        """
        if "data" not in flight_data:
            print("No flight data available.")
            if "error" in flight_data:
                print(f"Error: {flight_data['error']}")
            return

        # Filter flights based on min_price and max_price
        filtered_flights = [
            flight for flight in flight_data["data"]
            if (min_price is None or float(flight["price"]["total"]) >= min_price) and
               (max_price is None or float(flight["price"]["total"]) <= max_price)
        ]

        # Display filtered flights or top `max_results` if none match the price range
        if filtered_flights:
            print("Filtered Flight Options:")
            self.display_flights(filtered_flights)
        else:
            print(f"No flights found within the specified price range ({min_price} - {max_price}).")
            print(f"Displaying the top {max_results} available flights:")
            self.display_flights(flight_data["data"][:max_results])

    def display_flights(self, flights):
        """
        Helper method to display flight details in a readable format.

        Args:
            flights (list): List of flight offers to display.
        """
        for flight in flights:
            print(f"Flight ID: {flight['id']}")
            print(f"Price: {flight['price']['currency']} {flight['price']['total']}")
            for itinerary in flight["itineraries"]:
                print(f"  Duration: {itinerary['duration']}")
                for segment in itinerary["segments"]:
                    print(f"    {segment['carrierCode']} {segment['number']}: "
                          f"{segment['departure']['iataCode']} -> {segment['arrival']['iataCode']}")
                    print(f"    Departure: {segment['departure']['at']}, Arrival: {segment['arrival']['at']}")
            print("\n" + "-" * 50)
