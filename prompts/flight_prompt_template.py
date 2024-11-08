from langchain.prompts import PromptTemplate

# Prompt for origin
origin_prompt = PromptTemplate(
    input_variables=[],
    template="Where are you flying from?"
)

# Prompt for destination
destination_prompt = PromptTemplate(
    input_variables=["origin"],
    template="You're flying from {origin}. Where are you flying to?"
)

# Prompt for date
date_prompt = PromptTemplate(
    input_variables=["origin", "destination"],
    template="You're flying from {origin} to {destination}. What date are you planning to fly?"
)
