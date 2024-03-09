from selenium import webdriver
import time
from flask import Flask

app = Flask(__name__)

def get_driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print("An error occurred while creating the WebDriver:", e)
        return None

def get_page_title(url):
    driver = get_driver()
    if driver is None:
        return "Failed to create WebDriver"

    try:
        driver.get(url)
        time.sleep(5)
        page_title = driver.title
        return page_title
    except Exception as e:
        print("An error occurred while getting page title:", e)
        return "Failed to get page title"
    finally:
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print("An error occurred while quitting WebDriver:", e)

@app.route('/')
def index():
    page_title = get_page_title("https://www.example.com")
    return f"Page Title: {page_title}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
