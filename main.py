from selenium import webdriver
driver = webdriver. Chrome('C:/Users/User/Downloads/chromedriver.exe')
driver.get("https://www.flipkart.com")
driver.maximize_window()
#Close the pop-up
driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
#searching for iphones
search = driver.find_element_by_xpath("//body/div[@id='container']"
                            "/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/input[1]")
search.send_keys('iPhone')
#clicking enter
search.submit()

#CSV file
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

prices=[] #List to store price of the product
driver.get("https://www.flipkart.com/"
           "search?q=iPhone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'_2ZdXDB'}):
    price=a.find('div', attrs={'class':'_3xFhiH'})
    prices.append(price.text)

df = pd.DataFrame({'Price':prices})
df.to_csv('products.csv', index=False, encoding='utf-8')

