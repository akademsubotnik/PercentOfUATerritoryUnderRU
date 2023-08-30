# PercentOfUATerritoryUnderRU
PercentOfUATerritoryUnderRU

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
TODO: Understand why pylint github action is failing
