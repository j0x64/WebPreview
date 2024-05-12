# WebPreview is a Python program that allows you to preview any website home interface and turn it into an image
# Created by Jordan
# (C) MIT

# Defining some variables
blacklisted_web = ['pornhub.com', 'xnxx.com']

# Importing necessary libraries
import os
from time import sleep as wait
import asyncio
from pyppeteer import launch

# Creating main functions
async def capture_screenshot(url, save_path):
    browser = await launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.setViewport({'width': 1920, 'height': 1080})
    await page.screenshot({'path': save_path})
    await browser.close()

def check_website(input_website):
    if '.' in input_website:
        for website in blacklisted_web:
            if website in input_website:
                print(f"The website {input_website} is blacklisted.")
                return True
        return False

# Defining main class to run the functions
class Main():
    url = str('Input the website you wanted to capture: ')
    if not check_website(url):
        save_path = str('Where do you want to save the file: ')
        asyncio.get_event_loop().run_until_complete(capture_screenshot(url, save_path))
        print(f'File saved succesfully to {save_path}')

# Running all the functions
if __name__ == "__main__":
    Main()