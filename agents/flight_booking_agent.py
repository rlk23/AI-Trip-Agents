import requests
from config import FLIGHT_API_KEY, FLIGHT_API_SECRET, CHATGPT_API_KEY
from prompts.flight_prompt_template import origin_prompt, destination_prompt, date_prompt
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

class FlightBookingAgent:
    def __init__(self):
        self.access_token = None
        self.token_expiry = None

        # Initialize OpenAI LLM with the correct import and key
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=CHATGPT_API_KEY)
        self.origin_chain = LLMChain(llm=self.llm, prompt=origin_prompt)
        self.destination_chain = LLMChain(llm=self.llm, prompt=destination_prompt)
        self.date_chain = LLMChain(llm=self.llm, prompt=date_prompt)

    def authenticate(self):
        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": FLIGHT_API_KEY,
            "client_secret": FLIGHT_API_SECRET
        }
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            token_data = response.json()
            self.access_token = token_data["access_token"]
            self.token_expiry = token_data.get("expires_in")
        else:
            raise Exception("Failed to authenticate with Amadeus API: " + response.text)

    def get_access_token(self):
        if self.access_token is None or self.token_expiry is None:
            self.authenticate()
        return self.access_token

    def search_flights(self, origin, destination, departure_date):
        access_token = self.get_access_token()
        url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults": 1,
            "currencyCode": "USD",
            "max": 5
        }
        
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to retrieve flight offers: " + response.text)

    def book_flight(self, origin=None, destination=None, date=None):
        """Collect missing details and search for flights when all are provided."""

        # Check for missing information and prompt accordingly
        if not origin:
            prompt_output = self.origin_chain.predict()
            print(prompt_output)  # Show prompt to the user
            return prompt_output  # Expect the user to provide 'origin'

        if not destination:
            prompt_output = self.destination_chain.predict(origin=origin)
            print(prompt_output)
            return prompt_output  # Expect the user to provide 'destination'

        if not date:
            prompt_output = self.date_chain.predict(origin=origin, destination=destination)
            print(prompt_output)
            return prompt_output  # Expect the user to provide 'date'

        # If all details are provided, perform the flight search
        flight_data = self.search_flights(origin, destination, date)
        print("Flight search completed. Here are the results:")
        print(flight_data)
        return flight_data