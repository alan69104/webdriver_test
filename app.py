from selenium import webdriver
import time
from flask import Flask

app = Flask(__name__)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def get_page_title(url):
    driver = get_driver()
    driver.get(url)
    time.sleep(5)
    page_title = driver.title
    driver.quit()
    return page_title

@app.route('/')
def index():
    page_title = get_page_title("https://www.example.com")
    return f"Page Title: {page_title}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
