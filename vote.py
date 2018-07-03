from selenium import webdriver
from selenium.webdriver import ActionChains
import time

URL = "https://www.prephoops.com/2017/12/who-was-player-of-the-week-2/"

def vote(driver):
    checkBoxes = driver.find_elements_by_class_name("pds-answer-group")

    for box in checkBoxes:
        if "(Chicago U-High)" in box.get_attribute('innerHTML'):
            element = box.find_element_by_tag_name("label")
            break
    driver.execute_script("arguments[0].click();", element)
    voteBox = driver.find_element_by_id("pd-vote-button9899106")
    hover = ActionChains(driver)
    hover.move_to_element(voteBox)
    hover.click()
    hover.perform()
    time.sleep(5)

def run():
    while True:
        driver = webdriver.Chrome(executable_path="./chromedriver")
        try:

            driver.get(URL)
            vote(driver)
            driver.quit()
        except:
            driver.quit()
            run()

run()
