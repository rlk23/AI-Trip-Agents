from langchain import PromptTemplate # type: ignore

flight_details_prompt = PromptTemplate(
    input_variables=["origin", "destination", "date"],
    template="""
    Let's book your flight!
    {%- if origin == None -%}
    Where are you flying from?
    {%- elif destination == None -%}
    Where are you flying to?
    {%- elif date == None -%}
    What date are you planning to fly?
    {%- else -%}
    Confirming flight details:
    - From: {{ origin }}
    - To: {{ destination }}
    - Date: {{ date }}
    {%- endif -%}
    """
)
