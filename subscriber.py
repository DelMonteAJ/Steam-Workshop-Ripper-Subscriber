from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.steamcommunity.com")

annoyCheck = False
while "login" not in driver.current_url:
    if not annoyCheck:
        annoyCheck = True
        print("[+] Waiting for login page to load")
    sleep(0.1)
annoyCheck = False
while "login" in driver.current_url:
    if not annoyCheck:
        annoyCheck = True
        print("[+] Waiting for successful login")
    sleep(0.1)
print("[+] Logged in")
path = input("Enter a directory path to links.txt for downloading process:\nExample: C:\\Users\\User\\Desktop\\GModRip\\links.txt:\n")
print("\n")
folder = ""
if "links.txt" not in path:
    folder = path
    path = path + "\\links.txt"
    
else:
    folder = path
reader = open(path, "r")
lines = reader.readlines()
reader.close()
errorWriter = open(folder[0:-10] + "\\error.txt", "w")
count = 0
for line in lines:
    count += 1 
    link = line.split(" - ")[0]
    driver.get(link)
    try:
        element = driver.find_element(by=By.CLASS_NAME, value= "subscribeText")
        if "Subscribed" in element.text:
            print("[+] Already subscribed to " + link + "["+ str(count) + "/" + str(len(lines)) + "]\n\n")
        else:
            print("[+] Subscribed to " + link + "["+ str(count) + "/" + str(len(lines)) + "]\n\n")
            driver.find_element(by=By.ID, value= "SubscribeItemBtn").click()
    except Exception as e:
        print("[-] Error: This workshop may be unavailable! " + line.split(" - ")[1] + " - " + link + "\n")
        errorWriter.write(line) 

print("[+] Done")
errorWriter.close()
driver.close()