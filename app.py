from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/')
def index():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.binary_location = "/opt/render/project/.render/chrome/opt/google/chrome/chrome"  # Specify Chrome binary location

    # Set the path for ChromeDriver
    chromedriver_path = '/opt/render/project/.render/chromedriver-linux64/chromedriver'

    # Initialize the Chrome WebDriver service with the ChromeDriver path
    chrome_service = Service(chromedriver_path)

    # Initialize the Chrome WebDriver with the specified options and service
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    # Navigate to Google and get the page title
    driver.get("https://www.dcard.tw/f/utaipei")
    time.sleep(10)
    page_source = driver.page_source
    driver.quit()

    return f"網頁標題: {page_source}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
