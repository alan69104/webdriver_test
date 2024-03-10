from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def index():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

    # Set the path for ChromeDriver and Chrome
    chromedriver_path = '/opt/render/project/.render/chromedriver'
    chrome_options.binary_location = '/opt/render/project/.render/chrome/opt/google/chrome/google-chrome'

    # Initialize the Chrome WebDriver with the specified options
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
    
    # Example: Open Google and return a simple message
    driver.get("https://www.google.com")
    driver.quit()
    return "Google 主頁已打開"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
