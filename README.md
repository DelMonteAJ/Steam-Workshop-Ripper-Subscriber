# **Workshop Ripper/Subscriber** #
---
## Purpose
### These scripts are used to scrape all workshop links that the currently logged in user is subscribed to and writes the links to a file for the subscriber to mass subscribe to.
> Has to be the currently logged in user, due to Steam's privacy settings.

### The ideal audience is a group of friends attempting to synchronize workshop packages, such as for Garry's Mod. The hosting user would rip their workshop subscriptions and share the text file for the other friends to subscribe to using the respective Python3 scripts.
---
## Requirements
### Python 3 (Tested on 3.10.4)
### The following Python Modules: selenium

### To install selenium, type the following command into command prompt.
```bash
pip install selenium 
```

### You will also need a Chrome (or respective browser's) Driver for Selenium 
> For more details: [https://selenium-python.readthedocs.io/installation.html]

### Notes
#### If you use a different browser instead of Chrome, you will have to change the webdriver.Chrome() line to accomodate your driver.
#### Your driver will also need to be set on PATH, unless given a proper location in the program (refer to the selenium documentation for more info).
#### If the program install finished and the links.txt file is empty, give it a rerun as sometimes the webpage will not have enough time to properly load.
#### The subscriber assumes that the links file will be named links.txt and will not work correctly unless the program is adjusted for other naming conventions.
