# from flask import Flask, render_template, request
# from google import genai

# # Initialize the GenAI client with your API key
# client = genai.Client(api_key="AIzaSyCX6Pvyg8TINaMwM5Jt0DF6D_q7FP4eUYs")

# # System prompt to guide the assistant
# SYSTEM_PROMPT = "You are a virtual interview assistant. Respond to interview-related questions with relevant answers."

# # Function to get assistant response from Gemini API
# def get_assistant_response(question):
#     # The model is set to "gemini-2.0-flash" and we are generating content based on the user's question
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",  # Use the correct model name as per the documentation
#         contents=f"{SYSTEM_PROMPT} {question}"  # Combine system prompt with the user question
#     )

#     # The response object will contain the generated text
#     return response.text.strip() if response and response.text else "Sorry, I couldn't generate a response."

# # Create the Flask app
# app = Flask(__name__)

# # Route to render the web interface (index page)
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle user questions and return assistant responses
# @app.route('/ask', methods=['POST'])
# def ask():
#     user_input = request.form['question']
    
#     if user_input.lower() == "exit":
#         return render_template('index.html', response="Exiting the Virtual Interview Assistant. Goodbye!")
    
#     # Get the response from Gemini API
#     response = get_assistant_response(user_input)
    
#     # Render the response on the page
#     return render_template('index.html', response=response)

# # Run the Flask app
# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
from google import genai

# Initialize the GenAI client with your API key
client = genai.Client(api_key="AIzaSyCX6Pvyg8TINaMwM5Jt0DF6D_q7FP4eUYs")

# System prompt to guide the assistant
SYSTEM_PROMPT = "You are a virtual interview assistant. Respond to interview-related questions with relevant answers."

# Function to get assistant response from Gemini API
def get_assistant_response(question):
    # The model is set to "gemini-2.0-flash" and we are generating content based on the user's question
    response = client.models.generate_content(
        model="gemini-2.0-flash",  # Use the correct model name as per the documentation
        contents=f"{SYSTEM_PROMPT} {question}"  # Combine system prompt with the user question
    )

    # The response object will contain the generated text
    return response.text.strip() if response and response.text else "Sorry, I couldn't generate a response."

# Create the Flask app
app = Flask(__name__)

# Route to render the web interface (index page)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle user questions and return assistant responses
@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['question']
    
    if user_input.lower() == "exit":
        return render_template('index.html', response="Exiting the Virtual Interview Assistant. Goodbye!")
    
    # Get the response from Gemini API
    response = get_assistant_response(user_input)
    
    # Format the response for better readability (you can adjust as needed)
    structured_response = format_response(response)
    
    # Render the response on the page
    return render_template('index.html', response=structured_response)

# Helper function to format response text (optional)
def format_response(response_text):
    # Example formatting: You can structure the text with line breaks and bold text
    formatted_text = f"<p><strong>Interview Assistant says:</strong></p>"
    formatted_text += f"<p>{response_text.replace('* ', '<br><strong>* </strong>').replace('**', '<strong>').replace('**', '</strong>')}</p>"
    return formatted_text

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

