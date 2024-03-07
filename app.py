from selenium import webdriver
import time

# 使用 Chrome WebDriver
driver = webdriver.Chrome()

# 打開網頁
driver.get("https://www.example.com")

# 等待一段時間
time.sleep(5)

# 關閉瀏覽器
driver.quit()
