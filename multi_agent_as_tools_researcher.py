import logging
import random
from strands import Agent, tool
from strands_tools import http_request, calculator, file_write, python_repl, journal

# Define Model to use. Strands 1.0 defaults to us.anthropic.claude-sonnet-4-20250514-v1:0
#MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
MODEL_ID="us.anthropic.claude-3-7-sonnet-20250219-v1:0"
#MODEL_ID="us.anthropic.claude-3-5-sonnet-20241022-v2:0"

logging.getLogger("strands").setLevel(logging.DEBUG)

print("Enter an empty response to generate a random travel itinerary request.")
user_prompt = input("What help do you need with your travel plans? : ")
if not user_prompt.strip():
    questions = [
        "I have a business meeting in Singapore next week. Suggest a nice place to stay near the local startup scene, and suggest a few startups to visit",
        "I have a business trip covering Bangkok next Thursday and I need to visit multiple hospital customers. Suggest a nice place to stay that would be easy to get around to these hospitals."
    ]
    user_prompt = random.choice(questions)
print(f"Asked Question: {user_prompt}")

# Create specialized agents
research_analyst_agent = Agent(
    model=MODEL_ID,
    system_prompt="You are a research specialist who gathers and analyzes information about local startup markets",
    tools=[http_request, calculator, file_write, python_repl]
)

travel_advisor_agent = Agent(
    model=MODEL_ID,
    system_prompt="You are a travel expert who helps with trip planning and destination advice",
    tools=[http_request, journal]
)

# Convert the agents into tools
@tool
def research_analyst(query: str) -> str:
    response = research_analyst_agent(query)
    return str(response)

@tool
def travel_advisor(query: str) -> str:
    response = travel_advisor_agent(query)
    return str(response)

# Orchestrator naturally delegates to specialists
executive_assistant = Agent(
    model=MODEL_ID,
    tools=[research_analyst, travel_advisor] 
)

result = executive_assistant(user_prompt)