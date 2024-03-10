from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

app = Flask(__name__)

@app.route('/')
def index():
    chrome_path = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"
    chrome_driver_path = "/opt/render/project/.render/chromedriver"

    if os.path.exists(chrome_path) and os.path.exists(chrome_driver_path):
        try:
            chrome_options = Options()
            chrome_options.binary_location = chrome_path
            driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
            driver.get("https://www.google.com")
            print("Chrome launched successfully!")
            driver.quit()
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            return "Failed to launch Chrome"
    else:
        return "Chrome or ChromeDriver not found!"

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
