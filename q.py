import requests

def get_empathy_response(user_input):
    url = "https://gemini-api-endpoint.com/v1/empathy"  # Replace with actual Gemini API endpoint
    headers = {
        "Authorization": "Bearer YOUR_GEMINI_API_KEY",  # Replace with your Gemini API key
        "Content-Type": "application/json"
    }
    data = {
        "text": user_input
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {"text": "Sorry, I couldn't process your request at the moment."}
