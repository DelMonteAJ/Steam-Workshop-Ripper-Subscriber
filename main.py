from re import T
from shlex import split
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import codecs
from math import ceil
import os

def ripper(driver, path):
    link = input("Enter the link for steam profile's workshop items for that game:\nExample: https://steamcommunity.com/id/{Username}/myworkshopfiles/?appid=4000&browsefilter=mysubscriptions\n")
    pagesOfAddons = int(input("Enter how many addons:\nExample: 10\n"))
    pagesOfAddons = ceil(pagesOfAddons / 30)

    os.makedirs(path+"\\links", exist_ok=True)

    with open(path+"\\links\\links.txt", "w") as f:
        print("Clearing links.txt")
    n = os.path.join(path+"\\links", "source.txt")
    with open(n, "w") as f:
        print("Clearing source.txt")
    for i in range(1, pagesOfAddons + 1):
        newLink = link + "&p=" + str(i) + "&numperpage=30"

        driver.get(newLink)
        f = codecs.open(n, "a", "utf-8")

        while "mysubscriptions" not in driver.current_url or "login" in driver.current_url:
            sleep(0.1)

        f.write(driver.page_source)
        f.close()
    reader = codecs.open(n, "r", "utf-8")
    lines = reader.readlines()
    reader.close()
    upcoming = False
    count = 0
    f = codecs.open(path+"\\links\\links.txt", "a", "utf-8")
    for line in lines:
        
        if "workshopItemSubscriptionDetails" in line:
            upcoming = True

        else:
            if upcoming:
                upcoming = False
                line = line.lstrip("<a href=")
                line = line.lstrip("\"")
                line = line.split("\"><div")
                count += 1
                name = line[1]
                name = name.split(">")[1].split("<")[0]
                f.write(line[0]+ " - " + name + "\n")
                print(str(count) + " - " + line[0] + " - " + name)
    f.close()
    print("[+] Finished ripping")
    os.remove(n)

# def dependencyRun(driver, path):
#     reader = codecs.open(path + "\\dependencies.txt", "r", "utf-8")
#     lines = reader.readlines()
#     reader.close()
#     writer = open(path +"\\depend_out.txt", "w")

#     count = 0
#     links = []
#     for line in lines:
#         count += 1
#         if "https://steamcommunity.com/workshop/filedetails" in line and "filedetails/discussion" not in line:

#             sindex = line.find("https://steamcommunity.com/workshop/filedetails")
#             eindex = line[sindex:].find("target") + sindex
#             link = line[sindex:eindex-2]
#             if link not in links:
#                 links.append(link)
#                 writer.line(link)
#                 subscribe(driver, link)
#             continue

#     print(links)
#     writer.close()


def dependency(driver, path):
    reader = codecs.open(path + "\\depend.txt", "r", "utf-8")
    lines = reader.readlines()
    reader.close()
    count = 0
    links = []
    for line in lines:
        count += 1
        if "https://steamcommunity.com/workshop/filedetails" in line and "filedetails/discussion" not in line:

            sindex = line.find("https://steamcommunity.com/workshop/filedetails")
            eindex = line[sindex:].find("target") + sindex
            link = line[sindex:eindex-2]
            if link not in links:
                links.append(link)
                subscribe(driver, link, path)
            continue

def subscribe(driver, link, path):
    splitPath = path
    driver.get(link)
    try:
        element = driver.find_element(by=By.CLASS_NAME, value= "subscribeText")
        if "Subscribed" in element.text:
            print("[+] Already subscribed to " + link + "\n\n")
        else:
            print("[+] Subscribed to " + link + "\n\n")
            driver.find_element(by=By.ID, value= "SubscribeItemBtn").click()
            try:
                newE = driver.find_element(by=By.CLASS_NAME, value= "requiredItemsContainer")
                print("[-] Error: This workshop item has dependencies! " + link + "\n")
                with codecs.open(splitPath + "\\depend.txt", "w", "utf-8") as dWriter:
                    dWriter.write(driver.page_source)
                dependency(driver,splitPath)
                driver.get(link)
                if driver.find_element(by=By.CLASS_NAME, value= "subscribeText").text != "Unsubscribe" and driver.find_element(by=By.CLASS_NAME, value= "subscribeText").text != "Subscribed":
                        driver.find_element(by=By.ID, value= "SubscribeItemBtn").click()
            except:
                pass
    except Exception as e:
        print("[-] Error: This workshop may be unavailable! " + link + "\n")


def subscriber(driver, path):

    print("\n")

    path = path + "\\links\\links.txt"

    try:
        reader = open(path, "r")
    except FileNotFoundError:
        print("[-] links.txt cannot be found.\n")
        return
    lines = reader.readlines()
    reader.close()
    splitPath = path.split("\\links.txt")[0]
    errorWriter = open(splitPath + "\\error.txt", "w")
    dependWriter = codecs.open(splitPath + "\\dependencies.txt", "w", "utf-8")
    count = 0
    for line in lines:
        count += 1 
        link = line.split(" - ")[0]
        title = line.split(" - ")[1]
        driver.get(link)
        try:
            element = driver.find_element(by=By.CLASS_NAME, value= "subscribeText")
            if "Subscribed" in element.text:
                print("[+] Already subscribed to " + link + "["+ str(count) + "/" + str(len(lines)) + "]\n\n")
            else:
                
                driver.find_element(by=By.ID, value= "SubscribeItemBtn").click()
                try:
                    newE = driver.find_element(by=By.CLASS_NAME, value= "requiredItemsContainer")
                    print("[-] Error: This workshop item has dependencies! " + line.split(" - ")[1] + " - " + link + "\n")
                    errorWriter.write(link + " - " + title + " - Has dependencies!\n")
                    with codecs.open(splitPath + "\\depend.txt", "w", "utf-8") as dWriter:
                        dWriter.write(driver.page_source)
                    dependency(driver,splitPath)
                    driver.get(link)
                    
                    if driver.find_element(by=By.CLASS_NAME, value= "subscribeText").text != "Unsubscribe" and driver.find_element(by=By.CLASS_NAME, value= "subscribeText").text != "Subscribed":
                        driver.find_element(by=By.ID, value= "SubscribeItemBtn").click()
                    
                    
                    if driver.find_element(by=By.CLASS_NAME, value= "subscribeText").text == "Subscribe":
                        driver.find_element(by=By.ID, value= "SubscribeItemBtn").click()
                    print("[+] Subscribed to " + link + "["+ str(count) + "/" + str(len(lines)) + "]\n\n")
                    

                    # dependWriter.write(driver.page_source)
                except:
                    print("[+] Subscribed to " + link + "["+ str(count) + "/" + str(len(lines)) + "]\n\n")
                    pass
        except Exception as e:
            print("[-] Error: This workshop may be unavailable! " + line.split(" - ")[1] + " - " + link + "\n")
            errorWriter.write(line + " - Not avaiable!") 
    dependWriter.close()
    # dependencyRun(driver, splitPath)
    print("[+] Done")
    
    errorWriter.close()

running = True
print("[+] Starting")
path = input("Enter a directory path where the chromedriver is stored and where the links will be outputted: \nExample: C:\\Users\\User\\Desktop\\GModRip\\\n")
try:
    s = Service(path + "\\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    print("[+] Chrome driver found locally and loaded")
except:
    driver = webdriver.Chrome()
    print("[+] Chrome driver found in PATH and loaded")
driver.get("https://steamcommunity.com/login/home/?goto=")

# annoyCheck = False
# while "login" not in driver.current_url:
#     if not annoyCheck:
#         annoyCheck = True
#         print("[+] Waiting for login page to load")
#     sleep(0.1)
# annoyCheck = False
# while "login" in driver.current_url:
#     if not annoyCheck:
#         annoyCheck = True
#         print("[+] Waiting for successful login")
#     sleep(0.1)
print("[+] Logged in")


while running:
    selection = int(input("Enter the number corresponding with your choice:\n1. Ripper\n2. Subscriber\n3. Exit\n"))

    if selection == 1:
        ripper(driver, path)
    elif selection == 2:
        subscriber(driver, path)
    elif selection == 3:
        driver.close()
        running = False
    else:
        print("Invalid input")

