from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import time, ctime, sleep

#INPUT YOUR DETAILS HERE 

link = "" #Product link
Fname = "" #First Name
Lname = "" #Last Name 
phoneNumber = "" #Phone Number 
postCode = "" #Postcode
address1 = ""  #Street name
townName = ""   #Town
countyName = ""  #County
email = "" #Email
cardNumber = ""  #16 digit card number
cardCVV = ""   #3 digit cvv on back of card 
expiryMonth = ""   #Card expiry month
expiryYear = "" #card expiry year
buy = int("") #Type 1 to autobuy, type 2 to not buy

chromeDriverPath = ""  #Enter full path of the chrome driver which you are using


#SCRIPT 
    
browser = webdriver.Chrome(executable_path=chromeDriverPath)
browser.get(link)

browser.maximize_window() # For maximizing window
print("--------SCRIPT STARTING---------")
sleep(5)
browser.find_element_by_id("onetrust-accept-btn-handler").click()


GPUAvailable = False

while not GPUAvailable:

    try:
        BuyBTN = addButton = browser.find_element_by_css_selector(".Button__StyledButton-iESSlv.eyLozJ.Button-dtUzzq.sc-jfJzZe.kHUYTy.gdsrAv")
        print("Item is now available")
        GPUAvailable = True
    except:
        print("Unavailable")
        sleep(10)
        browser.refresh()
        
        
if GPUAvailable == True:
    sleep(1)#NEEDED
    browser.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[2]/section/div[3]/div[4]/div[1]/button").click()
    browser.get("https://www.currys.co.uk/app/basket")

    while True:
        try:
            browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/button").click() #press free delivery
            break
        except:
            pass
        
    while True: #enter postcode
        try:
            browser.find_element_by_css_selector(".sc-gJqsIT.sc-sPYgB.hvIzkn").send_keys(postCode)
            break
        except:
            pass
    
    while True:
        try:
            browser.find_element_by_css_selector(".sc-dHIava.ghoEse").click()
            break
        except:
            pass

    while True: #press Free button
        try:
            browser.find_element_by_css_selector(".Radio__Bullet-gRHULO.golegZ").click() 
            break
        except:
            pass
        
    while True: #press continue to details button
        try:
            browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div[5]/button").click()
            break
        except:
            pass

    while True:
        try:
            browser.find_element_by_css_selector(".Input__InputElement-fqaDsJ.hKxqfE").send_keys(email) #enter email
            break
        except:
            pass

    while True:
        try:
            browser.find_element_by_css_selector(".sc-iwsKbI.jqzWyn").click() #click continue button
            break
        except:
            pass

        
    while True:
        try:
            browser.find_element_by_css_selector(".Select__ReadOnlyInput-PDFUZ.jMXLis.Input__InputElement-dzCVaV.hlQxGP").click() #Select Title
            browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[1]/div/div/div[2]/div[2]").click()
            break
        except:
            pass

    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[2]/div/input").send_keys(Fname) #enter first name
    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[3]/div/input").send_keys(Lname) #enter last name
    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[4]/div/div/input").send_keys(phoneNumber) #enter phone number
    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[7]/div/input").send_keys(address1) #enter address
    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[9]/div/input").send_keys(address1) #enter City
    browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[1]/form/div[2]/div[2]/div[10]/div/input").send_keys(countyName) #enter county

    browser.execute_script("window.scrollTo(0, 1000);") #scroll down so confirm button is selectable
    
    while True:
        try:
            browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div/div[2]/button").click() #press confirm and continue button
            break
        except:
            pass
    
    while True:
        try:
            browser.find_element_by_id("payment-trigger").click() #select card button
            break
        except:
            pass

    while True:
        try:
            browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[1]/p[1]/input").send_keys(cardNumber) #enter card number
            break
        except:
            pass

    
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/p/span[3]/input[1]").send_keys(expiryMonth) #enter card expiry month
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/p/span[3]/input[2]").send_keys(expiryYear) #enter card expiry year
    browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/div/p/span[1]/span/input").send_keys(cardCVV) #enter card cvv
    
    if buy == 1:
        browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[1]/form/fieldset[1]/div[2]/p/span[3]/input[1]").click() #PRESSES BUY
    else:
        pass
