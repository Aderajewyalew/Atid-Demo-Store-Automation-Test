from Atid_Store.Test.sales_product import *
from Atid_Store.Test.end_to_end import *
from Atid_Store.Bases_Test.locaters import *

driver = webdriver.Chrome()
driver.get("https://atid.store/")
driver.maximize_window()

# Those functins drived from sales products file the first four function are tes upto carts
# the last one is test up to cart and also inclueded the procced to checkout

def test_e2e_all_catagories():
    store_buy_product()
    men_buy_product()
    women_buy_product()
    accesserios_product()
    accessry_second()

# Those functions are drived from sales products file
# The tset / functions are shows only sales product and the price are greater than 70 birr

def test_sales_products():
    sales_blue_shose()
    sales_yellow_shose()
    sales_blue_shorts()
    sales_gold_purs()


#  This function is add the product to the cart which have onlly five stars

def test_five_star_products():

    driver.find_element(By.XPATH,path).click()
    sleep(2)
    driver.find_element(By.XPATH,starrrrrr).click()
    sleep(3)
    driver.find_element(By.XPATH,add_cart).click()
    sleep(3)
    driver.find_element(By.XPATH,view_cart_five_star).click()
    sleep(3)



#  And also this function test the page where the customer fill all information about himself

def test_request_question():

    driver.find_element(By.XPATH, contact).click()
    sleep(2)
    coupon = driver.find_element(By.NAME, question)
    coupon.clear()
    coupon.send_keys(question_Value)
    sleep(2)
    coupon = driver.find_element(By.NAME, subject)
    coupon.clear()
    coupon.send_keys(subject_value)
    sleep(2)
    coupon = driver.find_element(By.NAME, email)
    coupon.clear()
    coupon.send_keys(question_value)
    sleep(2)
    coupon = driver.find_element(By.NAME, message)
    coupon.clear()
    coupon.send_keys(question_values)
    sleep(2)
    driver.find_element(By.XPATH, submit).click()
    sleep(2)
