import cloudscraper
from bs4 import BeautifulSoup
import requests
import time
import hashlib
import random
import os
import colorama
from colorama import Fore # i like pink text fuck you

colorama.init(autoreset=True)
scraper = cloudscraper.create_scraper()
print(Fore.LIGHTMAGENTA_EX +"VPNs and Proxies will break this bot.\n")

print(Fore.LIGHTMAGENTA_EX +"Put in a disboard tag")
tag = input(">>> ")

counter = 1
page = 1
image = 1

if os.path.exists('pfps') == False:
    os.mkdir('pfps')
if os.path.exists('pfps/'+tag.lower()) == False:
    os.mkdir('pfps/'+tag.lower())

response = scraper.get("https://disboard.org/servers/tag/"+tag.lower()+"/"+"1").text
soup = BeautifulSoup(response, 'html.parser')
soup = soup.find_all(class_ = "lazyload")
start = time.time()
while True:

    print(Fore.LIGHTMAGENTA_EX +"Counter: "+str(counter)+" Page: "+str(page)+" Image: "+str(image))

    try:
        print(Fore.MAGENTA+soup[counter]['data-src'])
        try:
            img_data = requests.get(soup[counter]['data-src']).content
            thing = hashlib.sha256(img_data).hexdigest();
            with open("pfps/"+tag+"/"+str(thing)+'.jpg', 'wb') as handler:
                handler.write(img_data)
            image = image + 1
            counter = counter + 1
        except:
            counter = counter + 1
            pass

    except IndexError:
        end = time.time()
        final = end - start
        final = str(round(final/60, 2))

        print(Fore.LIGHTMAGENTA_EX + "Elapsed Time: "+str(final)+" Minutes" )

        print(Fore.LIGHTMAGENTA_EX +"Waiting 7-10 seconds before grabbing another page.")
        time.sleep(random.randint(7,10))

        response = scraper.get("https://disboard.org/servers/tag/"+tag.lower()+"/"+str(page)).text
        soup = BeautifulSoup(response, 'html.parser')
        soup = soup.find_all(class_ = "lazyload")

        page = page + 1
        counter = 1
