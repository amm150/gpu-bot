from tkinter import *  # noqa: F403
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from threading import Thread
import time
import undetected_chromedriver as uc
import locale
from discord import Webhook, RequestsWebhookAdapter

locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

asusURL = 'https://shop.asus.com/us/90yv0kb2-m0aa00-rog-strix-rtx4080s-o16g-white.html'
neweggURL = 'https://www.newegg.com/asus-geforce-rtx-4080-super-rog-strix-rtx4080s-o16g-white/p/N82E16814126703'
bhURL = 'https://www.bhphotovideo.com/c/product/1807873-REG/asus_rog_strix_rtx4080s_o16g_white_geforce_rtx_4080_super.html'

"""  
project_name base module.

This is the principal module of the project_name project.
here you put your main classes and objects.

Be creative! do whatever you want!

If you want to replace this with a Flask application run:

    $ make init

and then choose `flask` as template.
"""

# example constant variable
NAME = "project_name"

# Browser class for opening and closing the webdriver
class Browser:
    def __init__(self):
        self.driver = None

    def close_browser(self):
        if not self.driver is None:
            stopSnipe.set('yes')
            self.driver.quit()

    def refresh(self):
        self.driver.refresh()

    def open_browser(self):
        # Close the browser if one is already open
        self.close_browser()

        self.driver = uc.Chrome(use_subprocess=True)
        self.driver.get(neweggURL)
    
    def get_driver(self):
        return self.driver

def startThread(function, name, arguments = ()):
    new_thread = Thread(target=function, name=name, args=arguments)
    new_thread.daemon = True
    new_thread.start()

def getElement(xPath):
    wait = WebDriverWait(browser.get_driver(), 10)
    element = wait.until(ec.visibility_of_element_located((By.XPATH, xPath)))

    return element

def clickElement(xPath):
    element = getElement(xPath)
    element.click()

def typeElement(xPath, value):
    input = getElement(xPath)
    browser.get_driver().execute_script("arguments[0].value=arguments[1];", input, value)

def sendDiscordMessage(message):
    webhook = Webhook.from_url(discordWebhookUrl, adapter=RequestsWebhookAdapter())
    webhook.send(message)

# Commands
def start_snipe():
    try:
        item = getElement('/html/body/div[29]/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div/span')

        inStock = 'no'

        if 'OUT OF STOCK' not in item.text:
            inStock = 'yes'
            sendDiscordMessage('IN STOCK: ' + neweggURL)

        if inStock == 'yes':
            time.sleep(pauseInterval)
        else:
            time.sleep(searchInterval)
            browser.refresh()
            time.sleep(3)
            start_snipe()
    except Exception as e:
        print(e)
        time.sleep(searchInterval)
        browser.refresh()
        time.sleep(3)
        start_snipe()

def start_snipe_thread():
    stopSnipe.set('no')
    startThread(start_snipe, 'startSnipe')

def stop_snipe():
    stopSnipe.set('yes')

def initialize():
    browser.open_browser()


# Instantiate browser class
browser = Browser()

app = Tk()

# Variables
stopSnipe = StringVar(value='no')

discordWebhookUrl = 'https://discord.com/api/webhooks/1204630676851134464/HW3pihTZ1lLyolMPovOuGfOkhee8_ptBceMDkRbDgUG87Hsg2yaknL3M-qq0uqLmJEF3'

searchInterval = 30
pauseInterval = 900
