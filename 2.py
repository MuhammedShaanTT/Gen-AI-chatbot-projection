import subprocess
import sys

def run_chatbot():
    try:
        # Run the Flask app
        subprocess.check_call([sys.executable, "app.py"])
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running chatbot: {e}")

if __name__ == "__main__":
    run_chatbot()
