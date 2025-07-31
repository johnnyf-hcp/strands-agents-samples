import logging  
import random
from strands import Agent 
from strands.multiagent import GraphBuilder, Swarm
from strands_tools import mem0_memory, calculator, file_write 

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


researcher_agents = [
    Agent( 
        name="medical_researcher", 
        model=MODEL_ID,
        system_prompt="You research medical topics thoroughly using your memory and built-in knowledge", 
        tools=[mem0_memory]
    ),
    Agent( 
        name="technology_researcher", 
        model=MODEL_ID,
        system_prompt="You research technology topics thoroughly using your memory and built-in knowledge", 
        tools=[mem0_memory]
    ),
    Agent( 
        name="economic_researcher", 
        model=MODEL_ID,
        system_prompt="You research economic topics thoroughly using your memory and built-in knowledge", 
        tools=[mem0_memory]
    )
]

analyst = Agent( 
    name="analyst", 
    model=MODEL_ID,
    system_prompt="You analyze data and create insights", 
    tools=[calculator, mem0_memory] 
)

checker = Agent( 
    name="checker", 
    model=MODEL_ID,
    system_prompt="You fact check data and reports using your memory and built-in knowledge", 
    tools=[mem0_memory] 
) 

writer = Agent( 
    name="writer", 
    model=MODEL_ID,
    system_prompt="You write comprehensive reports based on research and analysis", 
    tools=[file_write, mem0_memory] 
) 

# Create a swarm of researcher agents
research_swarm = Swarm(researcher_agents)

# Build the graph
builder = GraphBuilder()

# Add nodes
builder.add_node(research_swarm, "research")
builder.add_node(analyst, "analysis")
builder.add_node(checker, "fact_check")
builder.add_node(writer, "report")

# Add edges (dependencies)
builder.add_edge("research", "analysis")
builder.add_edge("research", "fact_check")
builder.add_edge("analysis", "report")
builder.add_edge("fact_check", "report")

# Set entry points (optional - will be auto-detected if not specified)
builder.set_entry_point("research")

# Build the graph
graph = builder.build()

# Execute the graph on a task
result = graph(user_prompt)

# Access the results
print(f"\nStatus: {result.status}")
print(f"Execution order: {[node.node_id for node in result.execution_order]}")
