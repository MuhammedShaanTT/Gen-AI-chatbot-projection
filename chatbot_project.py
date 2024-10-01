import requests
import json

def send_message(message):
    url = "http://127.0.0.1:5000/chat"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'message': message
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        
        if response.status_code == 200:
            chatbot_response = response.json()
            return chatbot_response
        else:
            return {"error": "Failed to get response from the server."}
    
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending chat session.")
            break
        
        response = send_message(user_input)
        
        if 'chatbot_response' in response:
            print("Chatbot: " + response['chatbot_response'])
        elif 'error' in response:
            print("Error: " + response['error'])
