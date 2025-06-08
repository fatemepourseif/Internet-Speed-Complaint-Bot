from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR_EMAIL"
TWITTER_PASSWORD = "YOUR_PASSWORD"
USERNAME = "YOUR_USERNAME"
CHROME_DRIVER_PATH = "YOUR_DRIVER_PATH"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")

        time.sleep(2)
        accept_button = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
        accept_button.click()
        time.sleep(2)
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
        go_button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"down : {self.down}\nup : {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(2)
        username_input = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
        username_input.send_keys(USERNAME)
        username_input.send_keys(Keys.ENTER)
        time.sleep(2)
        password_input = self.driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)
        accept_cookies = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div[2]/button[1]/div/span/span')
        accept_cookies.click()
        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/span')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        post_btn = self.driver.find_element(By.XPATH,
                                            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post_btn.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
