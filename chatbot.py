from openai import OpenAI

# Initialize the OpenAI API
client = OpenAI(api_key="<API_KEY>")

#Initialize conversation list
conversation = [
  {"role": "system", "content": "You are a helpful assistant"}
]

# Function to interact with GPT-3
def chat_with_gpt3(prompt, conversation):
  model_engine = "gpt-3.5-turbo" # You can choose other models depending on your use-case

  conversation.append({"role": "user", "content": prompt})

  # Make an API call to get a response from the model
  response = client.chat.completions.create(
    model=model_engine,
    messages=conversation
  )

  message_output = response.choices[0].message.content

  conversation.append({"role": "assistant", "content": message_output})

  return message_output

# Main chat loop
if __name__ == "__main__":
  print("Chatbot initialized. Type 'quit' to exit.")
  while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
      print("Chatbot: Goodbye!")
      break
    else:
      bot_response = chat_with_gpt3(user_input, conversation)
      print(f"Chatbot: {bot_response}")
