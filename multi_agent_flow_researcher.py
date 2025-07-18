# Ref: https://strandsagents.com/latest/examples/python/agents_workflows/
from strands import Agent
from strands_tools import http_request
import random

# Define Model to use. Strands 1.0 defaults to us.anthropic.claude-sonnet-4-20250514-v1:0
#MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
MODEL_ID="us.anthropic.claude-3-7-sonnet-20250219-v1:0"
#MODEL_ID="us.anthropic.claude-3-5-sonnet-20241022-v2:0"

# Researcher Agent with web capabilities
researcher_agent = Agent(
    #callback_handler=None, # suppresses output
    model=MODEL_ID,
    system_prompt=(
        "You are a Researcher Agent that gathers information from the web. "
        "1. Determine if the input is a research query or factual claim "
        "2. Use your research tools (http_request, retrieve) to find relevant information "
        "3. Include source URLs and keep findings under 500 words"
    ),
    tools=[http_request]
)

# Analyst Agent for verification and insight extraction
analyst_agent = Agent(
    #callback_handler=None, # suppresses output
    model=MODEL_ID,
    system_prompt=(
        "You are an Analyst Agent that verifies information. "
        "1. For factual claims: Rate accuracy from 1-5 and correct if needed "
        "2. For research queries: Identify 3-5 key insights "
        "3. Evaluate source reliability and keep analysis under 400 words"
    ),
)

# Writer Agent for final report creation
writer_agent = Agent(
    model=MODEL_ID,
    system_prompt=(
        "You are a Writer Agent that creates clear reports. "
        "1. For fact-checks: State whether claims are true or false "
        "2. For research: Present key insights in a logical structure "
        "3. Keep reports under 500 words with brief source mentions"
    )
)

def run_research_workflow(user_input):
    # Step 1: Researcher Agent gathers web information
    print("\nResearching...\n")
    researcher_response = researcher_agent(
        f"Research: '{user_input}'. Use your available tools to gather information from reliable sources.",
    )
    research_findings = str(researcher_response)

    # Step 2: Analyst Agent verifies facts
    print("\nAnalyzing...\n")
    analyst_response = analyst_agent(
        f"Analyze these findings about '{user_input}':\n\n{research_findings}",
    )
    analysis = str(analyst_response)

    # Step 3: Writer Agent creates report
    print("\nGenerating report...\n")
    final_report = writer_agent(
        f"Create a report on '{user_input}' based on this analysis:\n\n{analysis}"
    )

    return final_report

print("Enter an empty response to generate a random topic.")
user_prompt = input("Enter a topic to research on: ")
if not user_prompt.strip():
    topics = [
        "The impact of social media on mental health",
        "The ethics of artificial intelligence in healthcare",
        "Climate change and its impact on global food security",
        "The role of technology in disaster preparedness and risk management",
        "The future of work in the age of automation",
        "The rise of e-commerce and its impact on small businesses",
        "The effects of globalization on income inequality"
    ]
    user_prompt = random.choice(topics)
print(f"Your topic: {user_prompt}")
print("\nThinking...\n")
run_research_workflow(user_prompt)
