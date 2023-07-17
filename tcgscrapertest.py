import requests
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# def main():
#     #chrome_driver_path = "D:/downloads/chromedriver_win32/chromedriver.exe"
#     options = Options()
#     #options.binary_location = chrome_driver_path
#     options.add_argument("--headless")  # Run Chrome in headless mode
#     driver = webdriver.Chrome(options=options)

#     url = "https://www.tcgplayer.com/product/488270/magic-universes-beyond-the-lord-of-the-rings-tales-of-middle-earth-the-one-ring-borderless?xid=pi1b39d751-b865-4dee-b94c-e6d6494dfc3a&page=1&Language=English.html"
#     driver.get(url)

#     price_elements = driver.find_elements(".price")
#     if price_elements:
#         for price_element in price_elements:
#             price = price_element.text
#             print(f"Price: {price}")
#     else:
#         print("Price not found")

#     driver.quit()

# if __name__ == "__main__":
#     main()

def main():
    session = HTMLSession()
    url = "https://www.tcgplayer.com/product/488270/magic-universes-beyond-the-lord-of-the-rings-tales-of-middle-earth-the-one-ring-borderless?xid=pi1b39d751-b865-4dee-b94c-e6d6494dfc3a&page=1&Language=English.html"
    #response = requests.get(url)
    response = session.get(url)
    print (response)

    response.html.render(timeout=30000, sleep=1)

    price_elements = response.html.find(".price")

    if price_elements:
        for price_element in price_elements:
            price = price_element.text
            print(f"Price: {price}")
        print(f"Price: {price}")
    else:
        print("Price not found")

    #print(response.html.html)


    #soup = BeautifulSoup(response.content, "html.parser")
    #elements = soup.find_all(class_="spotlight__price")

    #print (soup.prettify())

    #print (soup)

    #print (f"Elements: {elements}")
    #print (f"Elements: {len(elements)}")

if __name__ == "__main__":
    main()