from time import sleep
import pytest
from selenium import webdriver
driver = webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.by import By
from Atid_Store.Bases_Test.locaters import *


def sales_blue_shose():
    driver = webdriver.Chrome()
    driver.get(Website_sale)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, men_sale).click()
    nav = driver.find_element(By.XPATH, Nav_ul)
    na = nav.find_elements(By.TAG_NAME, Na_il)

    for n in na:
        if n.text == 'ATID Blue Shoes':
            n.click()
            break
    driver.find_element(By.XPATH, Blue_shoes_men).click()
    sleep(2)
    driver.find_element(By.XPATH, Blue_shoes_men_chart).click()
    sleep(2)
    driver.find_element(By.XPATH,View_chart).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, product_names).text
    assert product_name == "ATID Blue Shoes"
    sleep(2)

def sales_yellow_shose():
    driver = webdriver.Chrome()
    driver.get(Website_sale)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, men_sale).click()
    nav = driver.find_element(By.XPATH, Nav_ul)
    na = nav.find_elements(By.TAG_NAME, Na_il)
    driver.find_element(By.XPATH, men_sale).click()
    for n in na:
        if n.text == 'ATID Yellow Shoes':
            n.click()
            break
    driver.find_element(By.XPATH, yellow_shoes).click()
    sleep(2)
    driver.find_element(By.XPATH, yellow_shoes_chart).click()
    sleep(2)
    driver.find_element(By.XPATH, View_chart).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, product_names).text
    assert product_name == "ATID Yellow Shoes"
    sleep(2)

def sales_blue_shorts():
    driver = webdriver.Chrome()
    driver.get(Website_sale)
    driver.maximize_window()
    sleep(2)
    driver.find_element(By.XPATH, men_sale).click()
    gap = driver.find_element(By.XPATH, wom_ul)
    ga = gap.find_elements(By.TAG_NAME, wo_il)

    driver.find_element(By.XPATH, women_sale).click()
    for m in ga:
        if m.text == 'Blue Denim Shorts':
            m.click()
            break
    driver.find_element(By.XPATH, Blue_Denium_shorts).click()
    sleep(2)
    driver.find_element(By.XPATH, Blue_Denium_shorts_chart).click()
    sleep(2)
    driver.find_element(By.XPATH, View_chart).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, product_names).text
    assert product_name == "Blue Denim Shorts"
    sleep(2)


def sales_gold_purs():
    driver = webdriver.Chrome()
    driver.get(Website_sale)
    driver.maximize_window()
    sleep(2)
    gap = driver.find_element(By.XPATH, wom_ul)
    ga = gap.find_elements(By.TAG_NAME, wo_il)
    driver.find_element(By.XPATH, women_sale).click()
    for m in ga:
        if m.text == 'Bright Gold Purse With Chain':
            m.click()
            break
    driver.find_element(By.XPATH, Bright_gold_purse).click()
    sleep(2)
    driver.find_element(By.XPATH, Bright_gold_purse_chart).click()
    sleep(2)
    driver.find_element(By.XPATH, View_chart).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, product_price).text
    assert product_name == "80.00 ₪"
    sleep(2)
