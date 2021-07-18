# lines 3 through 6 pull some software code (called libraries) 
# off the internet that is needed to run the code
from time import sleep
from datetime import datetime
import requests
import json

# Make an API call to Coinbase and store the response
while True:
    # the words: requests.get is how python goes out on the internet
    # inside the parentheses you put the website you want python to go to
    response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/spot')
    # save the response to a variable called "data"
    data = response.json()
    # the data comes back in a form called JSON, which is very easy to read
    # it comes back as something called a dictionary, just like one looks up a word
    # in the dictionary and there is a explanation.  The JSON data comes back with 
    # a key (like "base") and a value (like "BTC")
    # it also come back with a second key ("amount") and a value (the current BTC price)
    x = (data["data"]["base"])
    y = ( data["data"]["amount"])
    print(' =======================')
    # get the current time
    now = datetime.now()
    # save it to a variable called current_time
    current_time = now.strftime("%H:%M:%S")
    # print current time
    print("Current Time =", current_time)
    # print currency and price
    print (x + ' ' +  y)   
    
    # wait two seconds and get the price again
    sleep(2)
