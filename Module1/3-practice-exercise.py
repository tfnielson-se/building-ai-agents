from litellm import completion
from typing import List, Dict


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(model="openai/gpt-4o", messages=messages, max_tokens=1024)
    return response.choices[0].message.content

# Practice Exercise

# First Prompt:
    # Ask the user what function they want to create
    # Ask the LLM to write a basic Python function based on the user’s description
    # Parse the response to separate the code from the commentary by the LLM
ask_user = input("What function do you want to create?")

message = [
    {"role": "system", "content": "You are a Python expert software engineer that prefers functional programming.",},
    {"role": "user", "content": ask_user}
]
response = generate_response(message)
print(response)

# Second Prompt:
    # Pass the code generated from the first prompt
    # Ask the LLM to add comprehensive documentation including:
    # Function description
    # Parameter descriptions
    # Return value description
    # Example usage
    # Edge cases
message = [
    {"role": "system", "content": "You are a Python expert software engineer that prefers functional programming.",},
    {"role": "user", "content": ask_user},
    {"role": "assistant", "content": response},
    {"role": "user", "content": "Add comprehensive documentation including: Function description, Parameter descriptions, Return value description, Example usage, Edge cases."}
]
response = generate_response(message)
print(response)

# Third Prompt:
    # Pass the documented code generated from the second prompt
    # Ask the LLM to add test cases using Python’s unittest framework
    # Tests should cover:
    # Basic functionality
    # Edge cases
    # Error cases
    # Various input scenarios
message = [
    {"role": "system", "content": "You are a Python expert software engineer that prefers functional programming.",},
    {"role": "user", "content": ask_user},
    {"role": "assistant", "content": response},
    {"role": "user", "content": "Add test cases using Python’s unittest framework. Tests should cover: Basic functionality, Edge cases, Error cases, Various input scenarios."}
]
response = generate_response(message)
print(response)