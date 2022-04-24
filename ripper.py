from time import sleep
from selenium import webdriver
import codecs
import os

link = input("Enter the link for steam profile:\nExample: https://steamcommunity.com/id/{Username}/myworkshopfiles/?appid=4000&browsefilter=mysubscriptions:\n")
path = input("Enter a directory path for ripping process:\nExample: C:\\Users\\User\\Desktop\\GModRip\\:\n")
pagesOfAddons = int(input("Enter the number of pages of addons you want to rip:\nExample: 10\n"))
driver = webdriver.Chrome()
os.makedirs(path+"\\links", exist_ok=True)

with open(path+"\\links\\links.txt", "w") as f:
    print("Clearing links.txt")
n = os.path.join(path+"\\links", "source.txt")
with open(n, "w") as f:
    print("Clearing source.txt")
for i in range(1, pagesOfAddons + 1):
    newLink = link + "&p=" + str(i) + "&numperpage=30"
    print(path)

    driver.get(newLink)
    f = codecs.open(n, "a", "utf-8")

    while "mysubscriptions" not in driver.current_url or "login" in driver.current_url:
        sleep(0.1)

    f.write(driver.page_source)
    f.close()
print("[+] Logged in")
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
driver.close()