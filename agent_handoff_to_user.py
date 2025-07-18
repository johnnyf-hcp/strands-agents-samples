from strands import Agent
from strands_tools import handoff_to_user
import os

# Define Model to use. Strands 1.0 defaults to us.anthropic.claude-sonnet-4-20250514-v1:0
#MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
MODEL_ID="us.anthropic.claude-3-7-sonnet-20250219-v1:0"
#MODEL_ID="us.anthropic.claude-3-5-sonnet-20241022-v2:0"

SYSTEM_PROMPT="""
You are an IT expert. Answer the user's IT support query. 
When you need more information, ask any required follow up questions and wait for a response from the user with the handoff_to_user tool.
If the user enter's a blank response, stop interaction and exit.
"""
# Set environment variable to be able to see instructions sent to handoff_to_user tool
os.environ["STRANDS_TOOL_CONSOLE_MODE"] = "enabled"

# Include the handoff_to_user tool in our agent's tool list
agent = Agent(
    system_prompt=SYSTEM_PROMPT,
    model=MODEL_ID,
    tools=[handoff_to_user]
    )
print(f"Model: {agent.model.config}\n")
user_prompt = input("What is your IT support question?")
if user_prompt.strip():
    # The agent calls the handoff_to_user tool which includes the question for the customer
    agent(user_prompt)
print("Exiting...")