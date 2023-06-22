"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import functools
flushprint = functools.partial(print, flush=True)

def asyncGetWeather(url):
    service = Service(executable_path='chromedriver.exe')
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(service=service,options=options)
    flushprint("Getting page...")
    driver.get(url)
    flushprint("waiting 3 seconds for dynamic data to load...")
    time.sleep(3)
    flushprint("Done ... returning page source HTML")
    render = driver.page_source
    driver.quit()
    return render


def remove_attribute_values_from_file(html_string):
    
    soup = BeautifulSoup(html_string, 'html.parser')
    for tag in soup.find_all(True):
        tag.attrs = {}
    return str(soup.prettify())



def get_weather_data(url):
    page = asyncGetWeather(url)
    soup = BeautifulSoup(page, 'html.parser')
    history = soup.find('lib-city-history-observation')
    if history is None:
        print("Could not find tag 'lib-city-history-observation'")
        return None
    else:
        formatted_html = remove_attribute_values_from_file(history.prettify())
        return formatted_html



#Test
#url = 'http://www.wunderground.com/history/weekly/KCHO/date/2020-12-31'
#print(get_weather_data(url))
