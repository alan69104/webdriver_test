from flask import Flask
import pyautogui
import os

app = Flask(__name__)

@app.route('/')
def index():
    chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"
    if os.path.exists(chrome_path):
        pyautogui.open(chrome_path)
        return "Chrome launched successfully!"
    else:
        return "Chrome not found!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
