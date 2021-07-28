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
import pandas as pd
import time
import pymongo
import requests
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():

    # Set up Splinter
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

    img_url = url + img_url
    # Get News
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_content = soup.find_all('div', class_='article_teaser_body')[0].text
    #title
    #news_title
    #news_content
    
    # JPL Featured Image
    featured_image_site = 'https://spaceimages-mars.com/'
    featured_image_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'
    browser.visit(featured_image_url)
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    image_site = soup.find_all(class_='showing fancybox-thumbs')
    #featured_image_url
    
    # Scrape Target 
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    tables
    
    mars_facts = tables[1]
    #mars_facts
    
    mars_facts_html = facts.to_html()
    #mars_facts_html
    
    mars_facts_html.strip()
    print(mars_facts_html)
    
    # hemispheres
    guss_url = 'https://marshemispheres.com/'

    # Cerebus Hemisphere Enhanced
    url1 = 'https://marshemispheres.com/images/full.jpg'
    # Schiaparalli Hemisphere Enhanced
    url2 = 'https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg'
    # Syrtis Major Hemisphere Enhanced
    url3 = 'https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg'
    # Valles Marineris Hemisphere Enhanced
    url4 = 'https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg  
        
    

    browser.visit(guss_url)  
    html = browser.html
    soup = BeautifulSoup(html,'html.parser')
    hemisphere_image_urls = soup.find('div',class_='description')
    #hemisphere_image_urls
    hemisphere_image_urls = [
    {"title": "Cerebus Hemisphere Enhanced", "img_url":url1},
    {"title": "Schiaparalli Hemisphere Enhanced", "img_url":url2},
    {"title": "Syrtis Major Hemisphere Enhanced", "img_url":url3},
    {"title": "Valles Marineris Hemisphere Enhanced", "img_url":url4}
    ]
    
    
    bigbaliwick = { 
        "news_title":news_title,
        "news_content":news_content,
        "featured_image_url":featured_image_url,
        "mars_facts":mars_facts,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    #    "mars_img": complete_url }
    #    "mars_comparison": tables[0],
    #    "mars_specs": tables[1]
    #}
    #    bigbaliwick = {
    #    "mars_img": img_url,
    #    "mars_comparison": tables[0],
    #    "mars_specs": tables[1]
    #}

    browser.quit()
    
    # Return Results
    return bigbaliwick

