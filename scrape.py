import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import datetime
import time


def namacheko(url):
    TODAYS_DATE = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # WEBDRIVER_PATH = "C:\\Users\\Jordan\\Documents\\webdriver\\chromedriver.exe"
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        soup = BeautifulSoup(driver.page_source, "html.parser")

        pieces = soup.find_all("h4")
        pieces_list = [item.string for item in pieces]
        items = pieces_list[0::2]
        prices = pieces_list[1::2]

        tuple_pieces = list(zip(items, prices))

        df = pd.DataFrame(tuple_pieces)
        df.columns = ["Item", "Price"]

    except Exception as e:
        print(f"Error due to {e}")

    finally:
        driver.quit()

        df.to_csv(f"""./xlsx/namacheko_{TODAYS_DATE}.csv""", index=False, encoding="utf-8")
