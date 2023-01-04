import dis
from time import sleep
import pytest
from selenium import webdriver
driver = webdriver.Chrome()
from selenium import webdriver
from selenium.webdriver.common.by import By
from Atid_Store.Bases_Test.locaters import *


def store_buy_product():

    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.maximize_window()
    driver.find_element(By.XPATH,store_button).click()
    sleep(2)
    driver.find_element(By.XPATH,abchor_bracelet).click()
    sleep(2)
    driver.find_element(By.XPATH, add_to_chart).click()
    sleep(2)
    driver.find_element(By.XPATH,view_prduct_chart).click()
    sleep(2)
    coupon_filed = driver.find_element(By.XPATH, coupon_box)
    sleep(2)
    coupon_filed.clear()
    coupon_filed.send_keys("1234vdbdsb")
    sleep(2)
    driver.find_element(By.XPATH, apply_copuon).click()
    sleep(2)
    productname = driver.find_element(By.XPATH, name_product).text
    assert productname == "Anchor Bracelet"
    productprice = driver.find_element(By.XPATH, product_price).text
    assert productprice == "250.00 ₪"


def men_buy_product():
    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.maximize_window()
    driver.find_element(By.XPATH,men_button).click()
    sleep(1)
    driver.find_element(By.XPATH,page_two).click()
    sleep(1)
    driver.find_element(By.XPATH,product_red_hoodies).click()
    sleep(1)
    driver.find_element(By.XPATH, add_to_chart_men).click()
    sleep(1)
    driver.find_element(By.XPATH,view_chart).click()
    sleep(1)
    name = driver.find_element(By.XPATH, product_name).text
    assert name == "Red Hoodie"
    coupon_filed = driver.find_element(By.XPATH, coupon_field)
    sleep(2)
    coupon_filed.clear()
    coupon_filed.send_keys("1234vdbdsb")
    sleep(2)
    driver.find_element(By.XPATH, aplly_cupon).click()
    product_price = driver.find_element(By.XPATH, price).text
    assert product_price == "150.00 ₪"
    sleep(3)


def women_buy_product():
    women_driver = webdriver.Chrome()
    women_driver.get("https://atid.store/")
    women_driver.maximize_window()
    women_driver.find_element(By.XPATH,women_button).click()
    sleep(1)
    women_driver.find_element(By.XPATH,click_shoulder_handbag).click()
    sleep(1)
    women_driver.find_element(By.XPATH, added_to_chart).click()
    sleep(1)
    women_driver.find_element(By.XPATH, view_to_chart).click()
    sleep(1)

    product_name = women_driver.find_element(By.XPATH, products_name).text
    assert product_name == "Black Over-the-shoulder Handbag"

    product_price1 = women_driver.find_element(By.XPATH, products_price1).text
    assert product_price1 == "85.00 ₪"
    copun_box = women_driver.find_element(By.XPATH, coupon_boxw)
    sleep(2)
    copun_box.clear()
    copun_box.send_keys("123321wed")
    sleep(2)
    women_driver.find_element(By.XPATH, click_copun)
    sleep(2)


def accesserios_product():
    accessrios = webdriver.Chrome()
    accessrios.get("https://atid.store/")
    accessrios.maximize_window()
    accessrios.find_element(By.XPATH,
                            f"{accesserios}").click()
    sleep(1)
    accessrios.find_element(By.XPATH,
                            f"{click_products}").click()
    sleep(1)

    accessrios.find_element(By.XPATH, f"{click_add_product}").click()
    sleep(1)
    accessrios.find_element(By.XPATH, f"{view_chart_acc}").click()
    sleep(1)

    product_name = accessrios.find_element(By.XPATH, f"{productName}").text
    assert product_name == "Boho Bangle Bracelet"

    product_price1 = accessrios.find_element(By.XPATH, f"{productPrice}").text
    assert product_price1 == "45.00 ₪"
    copun_box = accessrios.find_element(By.XPATH, f"{copupn_box}")
    sleep(2)
    copun_box.clear()
    copun_box.send_keys("123321wed")
    sleep(2)
    accessrios.find_element(By.XPATH, f"{click_copun}").click()
    sleep(2)


def accessry_second():

    driver = webdriver.Chrome()
    driver.get("https://atid.store/")
    driver.maximize_window()

    driver.find_element(By.XPATH, Accessry2).click()
    sleep(2)
    driver.find_element(By.XPATH, Product_acc2).click()
    sleep(2)
    driver.find_element(By.XPATH, add_to_cart).click()
    sleep(2)
    driver.find_element(By.XPATH, Cart_cheak_product).click()
    coupon_Box = driver.find_element(By.NAME, acce_coupon)
    coupon_Box.clear()
    coupon_Box.send_keys(Coupon_value_acc2)
    sleep(2)
    driver.find_element(By.XPATH, Coupone_appply).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, Product_name_acc2).text
    assert product_name == "Boho Bangle Bracelet"
    sleep(2)
    driver.find_element(By.XPATH, procced).click()
    sleep(2)
    driver.find_element(By.XPATH,click_login).click()

    uname = driver.find_element(By.NAME,username)
    sleep(2)
    uname.clear()
    uname.send_keys("selam")
    passward = driver.find_element(By.NAME,password)
    sleep(2)
    passward.clear()
    passward.send_keys(451263)
    driver.find_element(By.XPATH,login).click()
    sleep(5)
    driver.find_element(By.XPATH,click_login_copoun).click()
    sleep(5)
    copon_box = driver.find_element(By.XPATH,copon_path)
    copon_box.clear()
    copon_box.send_keys("4152,lkmj")
    sleep(2)
    driver.find_element(By.NAME,click_apply_copon).click()
    sleep(2)
    Box_fname = driver.find_element(By.NAME, first_name)
    Box_fname.clear()
    Box_fname.send_keys(enter_first_name)
    sleep(2)
    Box_lname = driver.find_element(By.NAME, last_name)
    Box_lname.clear()
    Box_lname.send_keys(enter_last_name)
    sleep(2)
    Box_company = driver.find_element(By.NAME, Company_name)
    Box_company.clear()
    Box_company.send_keys(enter_name)
    sleep(2)

    driver.find_element(By.XPATH, Country_Region).click()
    sleep(2)
    driver.find_element(By.XPATH, enter_CountrY).click()
    sleep(2)
    coupon = driver.find_element(By.NAME, Street_address)
    coupon.clear()
    coupon.send_keys(enter_Street_address)
    sleep(2)
    coupon = driver.find_element(By.NAME, Street_unit)
    coupon.clear()
    coupon.send_keys(enter_Street)
    sleep(2)
    coupon = driver.find_element(By.NAME, Postcode_ZIP)
    coupon.clear()
    coupon.send_keys(enter_Postcod)
    sleep(2)
    coupon = driver.find_element(By.NAME, city)
    coupon.clear()
    coupon.send_keys(enter_city)
    sleep(2)
    coupon = driver.find_element(By.NAME, phone)
    coupon.clear()
    coupon.send_keys(enter_Phone)
    sleep(2)
    coupon = driver.find_element(By.NAME, Email_address)
    coupon.clear()
    coupon.send_keys(enter_Email)
    sleep(2)
    driver.find_element(By.XPATH, order).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, Placeorder).text
    assert product_name == "Checkout"
    sleep(2)



