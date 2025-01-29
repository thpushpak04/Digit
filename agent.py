import google.generativeai as genai
import mysql.connector

# Set up Gemini API Key
genai.configure(api_key="AIzaSyDibbryO_jfUKTz9bB5vs3Hb7FTOYgIJXY")

# MySQL Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",   # Replace with your MySQL username
    password="132",  # Replace with your MySQL password
    database="chatbot"
)
cursor = conn.cursor()

# Variable to store the AI agent's name
agent_name = "rishua"  # You can change this value as needed

def save_to_db(user_input, agent_response):
    """Save conversation to MySQL database."""
    cursor.execute("INSERT INTO history (user, agent) VALUES (%s, %s)", (user_input, agent_response))
    conn.commit()

def get_chat_history(limit=5):
    """Retrieve the last 'limit' messages from MySQL database."""
    cursor.execute("SELECT user, agent FROM history ORDER BY id DESC LIMIT %s", (limit,))
    rows = cursor.fetchall()
    return "\n".join([f"User: {row[0]}\n{agent_name}: {row[1]}" for row in reversed(rows)])

def chat_with_gemini(user_input):
    """Generate AI response with chat history as context."""
    chat_context = get_chat_history(5)  # Fetch last 5 messages
    full_prompt = f"Previous conversation:\n{chat_context}\nUser: {user_input}\n{agent_name}:"
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(full_prompt)
    
    save_to_db(user_input, response.text)  # Store in database
    return response.text

def start_chat():
    """Start the chatbot loop."""
    print(f"Welcome to your AI agent, {agent_name}! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print(f"Goodbye from {agent_name}!")
            break
        response = chat_with_gemini(user_input)
        print(f"{agent_name}:", response)

# Start the chat loop
start_chat()

# Close the database connection when done
conn.close()
