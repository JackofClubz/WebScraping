import csv
import requests
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os 

# import the webdriver, chrome driver is recommended
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.set_page_load_timeout(2)
filename = ""
maxcount = 100
i=0
cwd = os.getcwd()
   
# function to check if the button is on the page, to avoid miss-click problem
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
    time.sleep(2)

#I tried
def more():
    snippet = driver.find_element_by_class_name('postSnippet')
    if len(snippet)>0:
        return True
    else:
        return False 
    

pages_to_scrape = 3
url = 'YOUR URL'
driver.get(url)
#to maximize the the tab 
driver.maximize_window()

# open the file to save the review
path_to_file = cwd+"\FILENAME.csv"
csvFile = open(path_to_file, 'a', encoding="utf-8-sig")
csvWriter = csv.writer(csvFile)

# change the value inside the range to save the number of reviews we're going to grab
for i in range(0, pages_to_scrape):

    # give the DOM time to load
    time.sleep(2) 

    # Click the "expand review" link to reveal the entire review.
    #driver.find_element_by_xpath(".//div[contains(@class, 'widgetEvCall')]").click()
    #<span class="taLnk ulBlueLinks" onclick="widgetEvCall('handlers.clickExpand',event,this);">More</span>

    # Now we'll ask Selenium to look for elements in the page and save them to a variable. First lets define a  container that will hold all the reviews on the page. In a moment we'll parse these and save them:
    container = driver.find_elements_by_xpath("//div[@data-reviewid]")

    # Next we'll grab the date of the review:
    #dates = driver.find_elements_by_xpath(".//span[contains(@class, 'ratingDate')]")
    
   # Now we'll look at the reviews in the container and parse them out

    for j in range(len(container)): # A loop defined by the number of reviews

        # Grab the rating
        rating = container[j].find_element_by_xpath(".//span[contains(@class, 'ui_bubble_rating bubble_')]").get_attribute("class").split("_")[3]
        # Grab the title
        title = container[j].find_element_by_xpath(".//span[contains(@class, 'noQuotes')]").text
        #Grab the review
        review = container[j].find_element_by_xpath(".//div[contains(@class, 'entry')]").text.replace("\n", "  ") 
        # if container[j].more() == True:
        #     postSnippet = container[j].find_element_by_xpath(".//div[contains(@class, 'postSnippet')]").text.replace('\n', ' ')
        # else: 
        #     postSnippet = 'NA' 
        #Grab the data
        #date = " ".join(dates[j].text.split(" ")[-2:])
        
        #Save that data in the csv and then continue to process the next review
        csvWriter.writerow([ rating, title, review])# postSnippet]) 
        
    # When all the reviews in the container have been processed, change the page and repeat            
    #driver.find_element_by_xpath('.//a[@class="ui_button nav next primary "]').click()

# When all pages have been processed, quit the driver
driver.quit()
