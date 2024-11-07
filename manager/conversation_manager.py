from agents.flight_booking_agent import FlightBookingAgent
from agents.hotel_booking_agent import HotelBookingAgent 
from agents.itinerary_agent import ItineraryAgent

class ConversationManager:

    def __init__(self):

        self.flight_agent = FlightBookingAgent(api_key="")
        self.hotel_agent = HotelBookingAgent(api_key="")
        self.itinerary_agent = ItineraryAgent(api_key="")


    def handle_input(self,user_input):

        if "flight" in user_input:
            self.active_agent  = self.flight_agent
        
        elif "hotel" in user_input:
            self.active_agent = self.hotel_agent
        elif "itinerary" in user_input:
            self.active_agent = self.itinerary_agent

        if self.active_agents:
            return self.active_agent.book_flight() if isinstance(self.active_agent, FlightBookingAgent) else (
                self.active_agent.book_hotel() if isinstance(self.active_agent, HotelBookingAgent) else 
                self.active_agent.create_itinerary()
            )
        else:
            return "I can help with flights, hotels, or itineraries. What would you like to Book?"
        
        