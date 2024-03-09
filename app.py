from selenium import webdriver

url = "https://www.youtube.com/"
keyword = "4k"
# 開啟 Chrome 瀏覽器
driver = webdriver.Chrome()
# 調整瀏覽器視窗大小
driver.set_window_size(1024, 960)
# 進入指定網址
driver.get(url)

# 等待搜尋結果加載完成
driver.implicitly_wait(10)

# 獲取網頁標題
page_title = driver.title
print("網頁標題:", page_title)

# 關閉瀏覽器
driver.quit()
