import logging
from strands import Agent
import random

# Enable debug logging (optional)
# logging.getLogger("strands").setLevel(logging.DEBUG)
# logging.basicConfig(
#     format="%(levelname)s | %(name)s | %(message)s",
#     handlers=[logging.StreamHandler()]
# )

# Create the Subject Expert agent
subject_expert = Agent(
    system_prompt="""You are a Computer Science Subject Expert specializing
    in explaining technical concepts clearly and concisely. Your expertise
    covers programming languages, data structures, algorithms, computer
    architecture, and software engineering principles.
    
    When explaining concepts:
    1. Start with a clear, concise definition
    2. Provide relevant examples to illustrate the concept
    3. Explain practical applications where applicable
    4. Avoid unnecessary jargon, but introduce important terminology
    5. Consider the learner's perspective and make complex topics accessible
    
    Your goal is to help learners build a solid understanding of computer
    science fundamentals.
    """
)

def interactive_session():
    print("Computer Science Subject Expert Agent (type 'exit' to quit)")
    print("-----------------------------------------------------------")
    print("Enter an empty response to generate a random question.")
    
    while True:
        # Get user input
        user_input = input("\nYour question: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break
        if not user_input.strip():
            questions = [
                "Explain the concept of recursion in programming.",
                "What is a class? What is a superclass?",
                "Explain the time and space complexities of arrays, linked lists, trees, and graphs.",
                "Explain the SOLID principles of object-oriented design.",
                "Can you explain consensus algorithms in distributed systems?",
                "Explain the difference between machine learning and deep learning."
            ]
            user_input = random.choice(questions)
        # Send the input to the agent, which will automatically print the response
        print(f"Asked Question: {user_input}")
        print("\nThinking...\n")
        subject_expert(user_input)

if __name__ == "__main__":
    interactive_session()