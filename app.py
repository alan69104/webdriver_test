# 載入需要的套件
from selenium import webdriver

# 建立一個Firefox的webdriver物件，並指定driver的路徑
browser = webdriver.Chrome(executable_path=${PATH}:/opt/render/project/.render/chrome/opt/google/chrome/)

# 連到我的網站
browser.get("https://kirin.idv.tw")

# 印出網頁的標題
print(browser.title)

# 關閉瀏覽器
browser.quit()
