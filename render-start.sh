#!/usr/bin/env bash

# 遇到错误时终止脚本
set -o errexit

STORAGE_DIR=/opt/render/project/.render

# ... [省略之前的 Chrome 安装步骤] ...

# 获取 Chrome 主版本号
CHROME_VERSION=$(google-chrome --product-version | cut -d '.' -f 1-3)
echo "Chrome 版本: $CHROME_VERSION"

# 获取与 Chrome 兼容的 ChromeDriver 最新版本号
CHROMEDRIVER_VERSION=$(wget -qO- "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
echo "ChromeDriver 兼容版本: $CHROMEDRIVER_VERSION"

# 安装 ChromeDriver
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
    echo "正在下载 ChromeDriver..."
    wget -P $STORAGE_DIR "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
    unzip $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR
    rm $STORAGE_DIR/chromedriver_linux64.zip
    echo "ChromeDriver 安装完成。"
else
    echo "从缓存中使用 ChromeDriver。"
fi

# ... [省略之后的步骤] ...
