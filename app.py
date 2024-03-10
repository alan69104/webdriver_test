from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
    chrome_options.add_argument("--no-sandbox") # Sandbox is not used in headless mode
    chrome_options.add_argument("--disable-dev-shm-usage") # Overcome limited resource problems

    # Set the path for ChromeDriver
    chrome_driver_path = os.getenv("CHROME_DRIVER_PATH", "/opt/render/project/.render/chromedriver")

    # Set the path for Google Chrome if necessary
    chrome_path = os.getenv("CHROME_PATH", "/opt/render/project/.render/chrome/opt/google/chrome/chrome")
    chrome_options.binary_location = chrome_path

    # Initialize the Chrome WebDriver and open Google
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.get("https://www.google.com")

    # Optional: Perform a search on Google (just for demonstration)
    search_box = driver.find_element_by_name('q')  # Find the search box
    search_box.send_keys('Hello World' + Keys.RETURN)  # Perform a search

    # Close the browser
    driver.quit()

    # Return a success message
    return "Google 主頁已打開，並執行了一次搜索。"

if __name__ == "__main__":
    # Start the Flask app on port 5000
    app.run(host="0.0.0.0", port=5000)
