#!/usr/bin/env bash
# exit on error
set -o errexit

STORAGE_DIR=/opt/render/project/.render
CHROME_VERSION="122.0.6261.111"

if [[ ! -d $STORAGE_DIR/chrome ]]; then
  echo "...Downloading Chrome"
  mkdir -p $STORAGE_DIR/chrome
  cd $STORAGE_DIR/chrome
  wget -nv "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chrome-linux64.zip"
  echo "...Extracting Chrome package"
  unzip -o -q chrome-linux64.zip
  rm chrome-linux64.zip
  cd - # Return to the previous directory
else
  echo "...Using Chrome from cache"
fi

# Add Chrome's location to the PATH
export PATH="${PATH}:${STORAGE_DIR}/chrome"

# Download and install the matching version of ChromeDriver
if [[ ! -f $STORAGE_DIR/chromedriver ]]; then
  echo "...Downloading ChromeDriver"
  wget -nv -P $STORAGE_DIR "https://storage.googleapis.com/chrome-for-testing-public/${CHROME_VERSION}/linux64/chromedriver-linux64.zip"
  echo "...Extracting ChromeDriver package"
  unzip -o -q $STORAGE_DIR/chromedriver-linux64.zip -d $STORAGE_DIR
  chmod +x $STORAGE_DIR/chromedriver
  rm $STORAGE_DIR/chromedriver-linux64.zip
else
  echo "...Using ChromeDriver from cache"
fi

# Add ChromeDriver's location to the PATH
export PATH="${PATH}:${STORAGE_DIR}"

echo "Deployment completed successfully."
# Add your own build commands below...
