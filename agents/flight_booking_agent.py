from prompts.flight_prompt_template import flight_details_prompt
from langchain import ConversationChain # type: ignore


class FlightBookingAgent:
    def __init__(self,api_key):
        self.api_key = api_key
        self.flight_chain = ConversationChain(prompt=flight_details_prompt)
    

    def book_flight(self, origin=None, destination=None, date=None):
        prompt_output = self.flight_chain.run({"origin": origin, "destination":destination, "date":date})
        if origin and destination and date:
            return self.search_flights(origin, destination, date)   
        else:
            return prompt_output
        
    def search_flight(self, origin, destination, date):
        # Code to search for flights
        return f"Searching for flights from {origin} to {destination} on {date}."

