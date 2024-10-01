from chatbot.gemini_api import get_empathy_response

def get_chatbot_response(user_input):
    # Get empathy-driven response from Gemini API
    empathy_response = get_empathy_response(user_input)
    return empathy_response.get('text', "Sorry, I couldn't understand that.")
