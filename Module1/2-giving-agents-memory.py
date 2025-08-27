from litellm import completion
from typing import List, Dict


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(model="openai/gpt-4o", messages=messages, max_tokens=1024)
    return response.choices[0].message.content


messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that prefers functional programming.",
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values in a dictionary.",
    },
]

response = generate_response(messages)
print(response)

messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that prefers functional programming.",
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values in a dictionary.",
    },
    # Here is the assistant's response from the previous step
    # with the code. This gives it "memory" of the previous
    # interaction.
    {"role": "assistant", "content": response},
    # Now, we can ask the assistant to update the function
    {"role": "user", "content": "Update the function to include documentation."},
]

response = generate_response(messages)
print(response)

# For the first request:
# def swap_keys_values(d):
#     return {v: k for k, v in d.items()}

# For the second request: (WITHOUT assistnat!)
# I'm not sure what function you're referring to. Can you clarify?

# Output: (WITH assistant!)

# def swap_keys_values(d):
#     """
#     Swaps the keys and values in the given dictionary.

#     Args:
#         d (dict): The input dictionary with unique values.

#     Returns:
#         dict: A new dictionary where the keys and values are swapped.

#     Raises:
#         ValueError: If the dictionary contains duplicate values, as they
#                     cannot be used as unique keys in the result.

#     Example:
#         >>> swap_keys_values({'a': 1, 'b': 2, 'c': 3})
#         {1: 'a', 2: 'b', 3: 'c'}
#         >>> swap_keys_values({'x': 10, 'y': 20})
#         {10: 'x', 20: 'y'}
#     """
#     if len(d.values()) != len(set(d.values())):
#         raise ValueError("Duplicate values detected. Cannot swap keys and values.")
#     return {v: k for k, v in d.items()}

# Key Takeaways

# No Inherent Memory: The LLM has no knowledge of past interactions unless explicitly provided in the current prompt (via messages).

# Provide Full Context: To simulate continuity in a conversation, include all relevant messages (both user and assistant responses) in the messages parameter.

# Role of Assistant Messages: Adding previous responses as assistant messages allows the model to maintain a coherent conversation and build on earlier exchanges. For an agent, this will allow it to remember what actions, such as API calls, it took in the past.

# Memory Management: We can control what the LLM remembers or does not remember by managing what messages go into the conversation. Causing the LLM to forget things can be a powerful tool in some circumstances, such as when we need to break a pattern of poor responses from an Agent.
