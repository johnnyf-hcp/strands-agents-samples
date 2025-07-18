import logging  
import random
from strands import Agent 
from strands.multiagent import Swarm 
from strands_tools import memory, calculator, file_write 

# Define Model to use. Strands 1.0 defaults to us.anthropic.claude-sonnet-4-20250514-v1:0
#MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
MODEL_ID="us.anthropic.claude-3-7-sonnet-20250219-v1:0"
#MODEL_ID="us.anthropic.claude-3-5-sonnet-20241022-v2:0"

logging.getLogger("strands").setLevel(logging.DEBUG)

print("Enter an empty response to generate a random research request.")
user_prompt = input("Enter your research request : ")
if not user_prompt.strip():
    questions = [
        "What is the history of AI since 1950? Create a comprehensive report",
        "What is the impact of AI on healthcare? Create a comprehensive report",
        "What is the impact of AI on education? Create a comprehensive report",
        "What is the impact of AI on finance? Create a comprehensive report",
        "What is the impact of AI on transportation? Create a comprehensive report",
        "What is the impact of AI on manufacturing? Create a comprehensive report",
        "What is the impact of AI on the environment? Create a comprehensive report",
        "What is the impact of AI on society? Create a comprehensive report",
        "What is the impact of AI on the world? Create a comprehensive report"
    ]
    user_prompt = random.choice(questions)
print(f"Asked Question: {user_prompt}")


researcher = Agent( 
    name="researcher", 
    model=MODEL_ID,
    system_prompt="You research topics thoroughly using your memory and built-in knowledge", 
    tools=[memory] 
) 

analyst = Agent( 
    name="analyst", 
    model=MODEL_ID,
    system_prompt="You analyze data and create insights", 
    tools=[calculator, memory] 
)

writer = Agent( 
    name="writer", 
    model=MODEL_ID,
    system_prompt="You write comprehensive reports based on research and analysis", 
    tools=[file_write, memory] 
) 

# Swarm automatically coordinates agents 
market_research_team = Swarm([researcher, analyst, writer]) 
result = market_research_team(user_prompt)