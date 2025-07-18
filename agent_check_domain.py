# Ref: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/
from strands import Agent
from strands.tools.mcp import MCPClient
from strands_tools import http_request
from mcp import stdio_client, StdioServerParameters
import random

# Define Model to use. Strands 1.0 defaults to us.anthropic.claude-sonnet-4-20250514-v1:0
#MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
MODEL_ID="us.anthropic.claude-3-7-sonnet-20250219-v1:0"
#MODEL_ID="us.anthropic.claude-3-5-sonnet-20241022-v2:0"

# Define a naming-focused system prompt
NAMING_SYSTEM_PROMPT = """
You are an assistant that helps to name open source projects.

When providing open source project name suggestions, always provide
one or more available domain names and one or more available GitHub
organization names that could be used for the project.

Before providing your suggestions, use your tools to validate
that the domain names are not already registered and that the GitHub
organization names are not already used.
"""

# Load an MCP server that can determine if a domain name is available
domain_name_tools = MCPClient(lambda: stdio_client(
    StdioServerParameters(command="uvx", args=["fastdomaincheck-mcp-server"])
))

# Use a pre-built Strands Agents tool that can make requests to GitHub
# to determine if a GitHub organization name is available
github_tools = [http_request]

with domain_name_tools:
    # Define the naming agent with tools and a system prompt
    tools = domain_name_tools.list_tools_sync() + github_tools
    #print(f"Tools: {tools}")
    naming_agent = Agent(
        system_prompt=NAMING_SYSTEM_PROMPT,
        model=MODEL_ID,
        tools=tools
    )
    print(f"Model: {naming_agent.model.config}\n")
    print("Enter an empty response to generate a random objective.")
    user_prompt = input("Enter your desired objective for your project name:")
    if not user_prompt.strip():
        questions = [
            "I need to name an open source project for building AI agents.",
            "A new GenAI investment fund with high grade robo investment tools",
            "A new crypto startup focusing on Asian markets and linkages to local asian currencies"
        ]
        user_prompt = random.choice(questions)
    # Run the naming agent with the end user's prompt
    print(f"Desired Objective: {user_prompt}")
    naming_agent(user_prompt)