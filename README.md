# Description
Selenium Python web scraper to gather information from APIs. Used previously for pricing and reviews. 

## Documentation

Selenium documentation:

* [User Manual](https://selenium.dev/documentation/)

API documentation:

* [JavaScript](https://seleniumhq.github.io/selenium/docs/api/javascript/)
* [Python](https://seleniumhq.github.io/selenium/docs/api/py/)

## Requirements

I did not use a package manager :(, the tool simply runs with any ipynb and uses pandas to save all downloads on .csv. 

* Windows users:
  *  Latest version of [Visual Studio](https://www.visualstudio.com/) with command line tools and build tools installed
  *  Import Pandas/csv and Requests
  *  Make sure you have the correct environment for jupyter ipynb. I use [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)


## Running the Tool

It's a simplistic tool, modeled after Chris Cahoover's [Selenium tool](https://github.com/cahoover/). The only hard part is understanding the HTML layout of the page you are scraping. 

### Driver

The driver automates a browser of choice - I use chrome but Selenium also accomodates different browsers. 
```sh
driver = webdriver.Chrome(ChromeDriverManager().install())
```
Driver methods will trigger an external browser page, this will be what the rest of the program will scrape.

### HTML Selectors/Headers

Selenium retrieves information on the APIs based on their HTML location, in this tool we use the WebObject's _Xpath_ to determine which elements of the API we would like to scrape. 

```sh
title = container[j].find_element_by_xpath(".//span[contains(@class, 'noQuotes')]").text
```
<img width="487" alt="image" src="https://user-images.githubusercontent.com/93539524/159172916-ded57345-2a0e-4e6c-9927-28c3850a5135.png"> <img width="199" alt="image" src="https://user-images.githubusercontent.com/93539524/159172961-4f1b4e72-9c0f-4c8d-ac29-19c9030729ff.png">
<img width="960" alt="image" src="https://user-images.githubusercontent.com/93539524/159173008-92bb1cad-d4f4-4974-bc2b-815ffa479111.png">
<img width="959" alt="image" src="https://user-images.githubusercontent.com/93539524/159173025-ce9c43d1-3e4f-4a5a-bfd5-de9fb40d52a4.png">


<!---
LanceT-Metyis/LanceT-Metyis is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
