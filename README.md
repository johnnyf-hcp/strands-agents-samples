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
- **multi_agent_researcher.py** - A demo of a multi-agent flow that researches the web, verifies the results, and generates a report

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