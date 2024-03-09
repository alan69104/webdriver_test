from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask

app = Flask(__name__)

def get_page_title(url):
    driver = get_driver()
    if driver is None:
        return "Failed to create WebDriver"

    try:
        driver.get(url)
        # 使用显式等待等待页面标题出现
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
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
    url = "https://www.example.com"  # 设置要获取标题的网页URL
    page_title = get_page_title(url)
    return f"Page Title: {page_title}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
