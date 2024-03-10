#!/usr/bin/env bash

# 遇到错误时终止脚本
set -o errexit

STORAGE_DIR=/opt/render/project/.render

if [[ ! -d $STORAGE_DIR/chrome ]]; then
    echo "正在下载 Chrome..."
    mkdir -p $STORAGE_DIR/chrome
    cd $STORAGE_DIR/chrome
    wget -P ./ https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
    dpkg -x ./google-chrome-stable_current_amd64.deb $STORAGE_DIR/chrome
    rm ./google-chrome-stable_current_amd64.deb
    cd $HOME/project/src # 确保我们返回到原本的位置
    echo "Chrome 安装完成。"
else
    echo "从缓存中使用 Chrome。"
fi

# 设置 Chrome 可执行文件的目录到环境变量 PATH
CHROME_DIR="/opt/render/project/.render/chrome/opt/google/chrome"
export PATH="$PATH:$CHROME_DIR"

# 调试信息
echo "CHROME_DIR 设置为: $CHROME_DIR"
ls -l "$CHROME_DIR/chrome"
which chrome

# 获取 Chrome 版本
CHROME_VERSION=$(google-chrome --product-version | cut -d '.' -f 1-3)
echo "Chrome 版本: $CHROME_VERSION"

# 安装 ChromeDriver
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
    echo "正在下载 ChromeDriver..."
    wget -P $STORAGE_DIR https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
    unzip $STORAGE_DIR/chromedriver_linux64.zip -d $STORAGE_DIR
    rm $STORAGE_DIR/chromedriver_linux64.zip
    echo "ChromeDriver 安装完成。"
else
    echo "从缓存中使用 ChromeDriver。"
fi

# 设置 ChromeDriver 执行路径到环境变量
CHROME_DRIVER_PATH="$STORAGE_DIR"
export PATH="$PATH:$CHROME_DRIVER_PATH"

# 调试信息
echo "CHROME_DRIVER_PATH 设置为: $CHROME_DRIVER_PATH"
ls -l "$CHROME_DRIVER_PATH/chromedriver"
which chromedriver

mkdir -p /tmp
# 在此添加您自己的构建命令...
