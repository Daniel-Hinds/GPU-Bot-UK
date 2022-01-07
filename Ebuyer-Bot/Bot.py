from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import time, ctime, sleep

#INPUT YOUR DETAILS HERE 

link = "" #Product link
Fname = "" #First Name
Lname = "" #Last Name 
phoneNumber = "" #Phone Number 
postCode = "" #Postcode
propertyNumber = ""  #House number/name
streetName = ""  #Street name
townName = ""   #Town
countyName = ""  #County
email = "" #Email
cardNumber = ""  #16 digit card number
cardCVV = ""   #3 digit cvv on back of card
cardHolderName = ""    #Card holders name 
cardExpiry = ""   #Card expiry
buy = int("") #Type 1 to autobuy, type 2 to not buy

chromeDriverPath = ""  #Enter full path of the chrome driver which you are using


#SCRIPT 
    
browser = webdriver.Chrome(executable_path=chromeDriverPath)
browser.get(link)

browser.maximize_window() # For maximizing window
print("--------SCRIPT STARTING---------")
browser.find_element_by_css_selector(".js-cookie-monster-accept").click()


GPUAvailable = False

while not GPUAvailable:

    try:
        BuyBTN = addButton = browser.find_element_by_css_selector(".js-add-to-basket-main.js-show-loader")
        print("Item is now available")
        GPUAvailable = True
    except:
        print("Unavailable")
        sleep(10)
        browser.refresh()
        
        
if GPUAvailable == True:
    print("Initiating checkout process")

    browser.find_element_by_css_selector(".js-add-to-basket-main.js-show-loader").click()     #adds to basket
    browser.find_element_by_css_selector(".checkout-radio.js-checkout-radio").click()
    browser.find_element_by_css_selector(".js-checkout-button").click()

    emailField = browser.find_element_by_css_selector(".text")
    emailField.send_keys(email)      #TYPE EMAIL HERE

    browser.find_element_by_xpath("//input[@value='Continue as Guest']").click()  #selects the continue as guest button

    firstName = browser.find_element_by_name("strFirstName")
    firstName.send_keys(Fname)        #TYPE FIRST NAME HERE

    lastName = browser.find_element_by_name("strLastName")
    lastName.send_keys(Lname)         #TYPE LAST NAME HERE

    phone = browser.find_element_by_name("strMobilePhoneNumber")
    phone.send_keys(phoneNumber)          #TYPE MOBILE NUMBER HERE

    post = browser.find_element_by_name("strShippingPostcode")
    post.send_keys(postCode)       #TYPE POST CODE HERE
    browser.find_element_by_class_name("cta-btn").click()

    while True:
        try:
            dropdown = Select(browser.find_element_by_id('js-select-shipping-address'))   #Select manual address from postcode dropdown
            dropdown.select_by_visible_text("Enter your address manually")
            break
        except:
            pass


    propertyName = browser.find_element_by_id('js-shipping-address-property')
    propertyName.send_keys(propertyNumber)
    
    street = browser.find_element_by_id('js-shipping-address-address1')
    street.send_keys(streetName)
    
    town = browser.find_element_by_id('js-shipping-address-town')
    town.send_keys(townName)
    
    county = browser.find_element_by_id('js-shipping-address-county')
    county.send_keys(countyName)

    payment = True          #waits until payment button is selectable then clicks
    while payment:
        
        try:
            browser.find_element_by_xpath("//input[@value='Continue to Payment']").click()
            payment = False
        except:
            pass


    frame = True
    while frame:
        
        try:
            browser.switch_to.frame(browser.find_element_by_tag_name("iframe"))
            browser.find_element_by_id("card-number").send_keys(cardNumber)
            browser.find_element_by_name("card_cvn").send_keys(cardCVV)
            browser.find_element_by_id("card-expiry").send_keys(cardExpiry)
            
            ####### THIS CLICKS BUY ######
            if buy == 1:
              #browser.find_element_by_css_selector(".order-button.cta-btn--secure").click()
              print("---------CHECKOUT COMPLETE--------")
            else:
                print("Item ready to buy!")
            
            frame = False
        except:
            pass
