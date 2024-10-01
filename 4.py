from flask import Flask, request, jsonify
from chatbot.chatbot import get_chatbot_response
from chatbot.nlp import analyze_input

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data['message']
    
    # Analyze user input with spaCy
    analysis = analyze_input(user_input)
    
    # Get chatbot response from Gemini API
    chatbot_response = get_chatbot_response(user_input)
    
    # Construct response to return to the frontend
    response_data = {
        'user_input_analysis': analysis,
        'chatbot_response': chatbot_response
    }
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
