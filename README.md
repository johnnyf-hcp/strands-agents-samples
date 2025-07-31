# Strands Demo

A demo project showcasing the Strands AI agent framework.

## Features and Available Scripts

- **agent_check_domain.py** - AI agent that suggests open source project names
  - Domain name availability checking via MCP server
  - GitHub organization name validation
  - Integration with fastdomaincheck-mcp-server
- **agent_check_weather.py** - AI agent that checks weather
  - Makes HTTP requests to the National Weather Service API
- **agent_do_math.py** - AI agent that does math
  - Uses calculator tool to solve maths questions
- **agent_do_science.py** - AI agent that is a computer science expert
- **agent_handoff_to_user.py** - AI agent that is an IT support expert that is able to ask user questions using the new handoff_to_user tool 
- **multi_agent_as_tools_researcher.py** - A demo of a executive assistant agent that helps to prepare a travel itinerary. This demonstrates how the agent can use two other agents (research analyst and travel advisor) as tools.
- **multi_agent_flow_researcher.py** - A demo of a multi-agent flow that researches the web, verifies the results, and generates a report
- **multi_agent_swarm_researcher.py** - A demo of the Strands swarm feature to coordinate multiple agents (researchers, writers, analysts) to work a market research team.
- **multi_agent_graph_researcher.py** - A demo of a Strands graph feature that 1/ researches the web with a swarm, 2/ verifies the results and fact checks in parallel, and 3/ generates a report. The graph feature demonstrates the ability to build a Directed Acyclic Graph (DAG) based agent orchestration flow where agent and swarms can be used as nodes in the graph.
- **A2A** folder - Contains a sample A2A server providing a calculator agent (a2a_agent_calculator.py) and a sample A2A client (a2a_client_async_calculator.py)

## Installation

```bash
brew install uv
pip install -r requirements.txt
```

## Usage

```bash
python <script name>.py
```

The agent will suggest project names along with available domain names and GitHub organization names.