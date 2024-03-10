from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

@app.route('/')
def index():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model

    # Set the path for ChromeDriver
    chromedriver_path = '/opt/render/project/.render/chromedriver-linux64/chromedriver'

    # Initialize the Chrome WebDriver service with the ChromeDriver path
    chrome_service = Service(chromedriver_path)

    # Initialize the Chrome WebDriver with the specified options and service
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    # Example: Open Google and return a simple message
    driver.get("https://www.google.com")
    driver.quit()
    return "Google 主頁已打開"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
