# GPU-Bot-UK
A python bot which can auto-checkout on the Curry's and Ebuyer website.

This bot uses the selenium webdriver to control a chrome browser, in both instances it checks the website for the add to cart button. 
If the button exists then it buys the item, else it refreshes the page (every 10 seconds) until the add to cart button exists.

# How To Use

Run `pip install -r requirements.txt`

Download the Chrome webdriver from here https://chromedriver.chromium.org/downloads

Open the Bot.py file using IDLE

Change the link to the link of the product you want to buy

Fill in your details where instructed

To auto-buy the item enter 1 | To stop the script before buying the item (for testing purposes) enter 2

Enter the FULL path of the chromedriver where instructed

Save the file and execute it

# How It Works

Selenium is a library which allows you to control the chrome (and firefox) web browser using python. Due to this the bot can navigate webpages by making use of classes, IDs or xpaths of the HTML. 

The bot checks if an item is in stock by refreshing a specified webpage (every 10 seconds) until it detects the add to cart button appear by checking for its class. When it appears it clicks the button and initiates the rest of the program which executes the checkout process.


# Extra Info

The python selenium webdriver is quite RAM intensive and is known to crash from time to time.

How quickly the bot checks whether its in stock can be changed by adjusting the sleep() in the while loop. Beware, reducing this time (therefore refreshing the website too quickly) could result in you getting time out or banned via your IP address. 

# Email Notifications

If you want an email when the bot has bought the item you have been waiting for, copy and paste the code from the Email-Notifications section to the bottom of the Bot.py file. 

Change the usernames, email and password to your own gmail account

Some Gmail accounts have extra security measures which may have to be disabled.

# Credits 

Daniel Hinds
