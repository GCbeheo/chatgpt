import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Start a conversation loop
while True:
    # Create a variable to accept input
    user_input = input("You: ")

    # Check if the user wants to exit
    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break

    # Send the user input to the API and stream the response
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": user_input},
        ],
        stream=True,
    )

    # Print the response from ChatGPT
    print("ChatGPT: ", end="")
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    print()  # Print a newline character for better formatting
