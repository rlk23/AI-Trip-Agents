from agents.flight_booking_agent import FlightBookingAgent

def main():
    flight_agent = FlightBookingAgent()

    # Initialize details as None to start the prompting process
    origin, destination, date = None, None, None

    while not (origin and destination and date):
        # Collect missing details and get a response
        if not origin:
            prompt_output = flight_agent.book_flight(origin, destination, date)
            origin = input("User: ")  # Provide input for origin
        
        elif not destination:
            prompt_output = flight_agent.book_flight(origin, destination, date)
            destination = input("User: ")  # Provide input for destination

        elif not date:
            prompt_output = flight_agent.book_flight(origin, destination, date)
            date = input("User: ")  # Provide input for date

    # Perform the final booking search once details are complete
    print("All details gathered, performing flight search.")
    flight_results = flight_agent.book_flight(origin, destination, date)
    print(flight_results)

if __name__ == "__main__":
    main()
