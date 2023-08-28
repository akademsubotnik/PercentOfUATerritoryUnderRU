# PercentOfUATerritoryUnderRU
PercentOfUATerritoryUnderRU

This repository will try to show what percent of UA terriorty is under RU control
How DO?
<img width="1080" alt="image" src="https://github.com/akademsubotnik/PercentOfUATerritoryUnderRU/assets/44036625/c5fbd3af-6ec0-4786-ad96-80a63504f44d">

Steps to run 
NOTE: Docker image contains everything, but if you want to use the below method, you will need to have google-chrome v116.0.5485.96 (located in chromedriver-linux64/LATEST_RELEASE_116.0.5845) , python3, pip installed.  This repository contains selenium chrome driver
You can follow this site to run locally
  1. $git clone https://github.com/akademsubotnik/PercentOfUATerritoryUnderRU.git
  2. $cd PercentOfUATerritoryUnderRU
  3. $source uaru/bin/activate
  4. $pip install -r requirements.txt
  5. $python3 main.py

Docker image : docker pull akademsubotnik/ruoccupyua

TODO: Pin version of chrome to be v116.0.5485.96 in DOCKERFILE!!!
TODO: Add some github actions to this repo!!!

USEFUL PAGES:
https://stackoverflow.com/questions/76428561/typeerror-webdriver-init-got-multiple-values-for-argument-options
https://googlechromelabs.github.io/chrome-for-testing/#stable
https://chromedriver.chromium.org/downloads
https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints
https://linuxhint.com/install_google_chrome_ubuntu_ppa/
https://stackoverflow.com/questions/22424737/unknown-error-chrome-failed-to-start-exited-abnormally
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
