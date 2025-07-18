# Basic A2A Server
import logging
from strands_tools.calculator import calculator
from strands import Agent
from strands.multiagent.a2a import A2AServer

logging.basicConfig(level=logging.INFO)

# Create a Strands agent
strands_agent = Agent(
    name="Calculator Agent",
    description="A calculator agent that can perform basic arithmetic operations.",
    tools=[calculator],
    callback_handler=None
)

# Create A2A server (streaming enabled by default)
"""
The A2AServer constructor accepts several configuration options:
agent: The Strands Agent to wrap with A2A compatibility
host: Hostname or IP address to bind to (default: "0.0.0.0")
port: Port to bind to (default: 9000)
version: Version of the agent (default: "0.0.1")
skills: Custom list of agent skills (default: auto-generated from tools)
"""
a2a_server = A2AServer(agent=strands_agent)

# Start the server
a2a_server.serve()