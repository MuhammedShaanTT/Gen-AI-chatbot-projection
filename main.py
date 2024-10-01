import subprocess
import sys

def install_dependencies():
    # Install Flask, Requests, and spaCy
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "requests", "spacy"])
    
    # Download the spaCy language model
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])

if __name__ == "__main__":
    install_dependencies()
