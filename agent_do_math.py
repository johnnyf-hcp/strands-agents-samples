from strands import Agent
from strands_tools import calculator
import random

agent = Agent(tools=[calculator])
print("Enter an empty response to generate a random question.")
user_prompt = input("Enter your math question: ")
if not user_prompt.strip():
    questions = [
        "What is the square root of 144?",
        "Calculate 15% of 240",
        "What is 7 factorial?",
        "Find the area of a circle with radius 5",
        "What is 2 to the power of 8?",
        "Calculate the hypotenuse of a right triangle with sides 3 and 4"
    ]
    user_prompt = random.choice(questions)
print(f"Asked Question: {user_prompt}")
agent(user_prompt)