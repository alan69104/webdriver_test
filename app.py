from flask import Flask
import pyautogui
import os

app = Flask(__name__)

@app.route('/')
def index():
    chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"
    if os.path.exists(chrome_path):
        try:
            pyautogui.open(chrome_path)
            print("Chrome launched successfully!")
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return "Failed to launch Chrome"
    else:
        return "Chrome not found!"

    # 添加調試代碼
    import subprocess
    cmd = ["ps", "aux"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()
    print("Process list:")
    print(output.decode())

    return "Chrome launched successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
