#####################################################################################
####
####   Missions to Mars 
####       Dan C. 
####
#####################################################################################
# Import BeautifulSoup
from bs4 import BeautifulSoup

# Import Splinter and set the chromedriver path
from splinter import Browser

import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():

    executable_path = {"executable_path": "chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)

    # Visit the following URL
    url = "https://spaceimages-mars.com"
    browser.visit(url)
    
    time.sleep(1)

    xpath = "/html/body/div[1]/img"
    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find("img", class_="headerimage")["src"]
    #img_url

    # Import Pandas
    import pandas as pd

    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    #tables
    
    # Close the browser after scraping
    browser.quit()
    
    # Return Results
    resturn tables

