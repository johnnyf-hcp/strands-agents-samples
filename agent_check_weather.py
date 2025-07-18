# Ref: https://catalog.us-east-1.prod.workshops.aws/workshops/4b60df1c-f594-4728-8683-be2f7598a60f/en-US/module-2-building-weather-agent-with-strands
from strands import Agent
from strands_tools import http_request
import random
import os

# Define Model to use. Strands 1.0 defaults to us.anthropic.claude-sonnet-4-20250514-v1:0
#MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
MODEL_ID="us.anthropic.claude-3-7-sonnet-20250219-v1:0"
#MODEL_ID="us.anthropic.claude-3-5-sonnet-20241022-v2:0"

# Define a weather-focused system prompt
WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:

1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States

When retrieving weather information:
1. First get the coordinates or grid information using https://api.weather.gov/points/{latitude},{longitude} or https://api.weather.gov/points/{zipcode}
2. Then use the returned forecast URL to get the actual forecast

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.
"""
# Set environment variable to be able to see instructions sent to handoff_to_user tool
os.environ["STRANDS_TOOL_CONSOLE_MODE"] = "enabled"

# Create an agent with HTTP capabilities
agent = Agent(
    system_prompt=WEATHER_SYSTEM_PROMPT,
    model=MODEL_ID,
    tools=[http_request],  # Explicitly enable http_request tool
)
print(f"Model: {agent.model.config}\n")
print("Enter an empty response to generate a random US city.")
user_prompt = input("Enter your weather question for US Cities: ")
if not user_prompt.strip():
    cities = [
        "Seattle",
        "Maimi, Florida",
        "New York",
        "Chicago",
        "Los Angeles",
        "Austin"
    ]
    user_prompt = random.choice(cities)
print(f"Your Question: {user_prompt}")
agent(user_prompt)