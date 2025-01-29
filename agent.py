import google.generativeai as genai

# Set up Gemini API Key
genai.configure(api_key="AIzaSyDibbryO_jfUKTz9bB5vs3Hb7FTOYgIJXY")

def chat_with_gemini(user_input):
    # Set the model to "gemini-pro"
    model = genai.GenerativeModel("gemini-pro")
    # Generate a response using the model
    response = model.generate_content(user_input)
    return response.text

# Function to simulate chat with the agent
def start_chat():
    print("Welcome to your AI agent! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        # Get the AI response
        response = chat_with_gemini(user_input)
        print("Agent: ", response)

# Start the chat loop
start_chat()
