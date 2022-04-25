# **Workshop Ripper/Subscriber** #
---
## Purpose
### These scripts are used to scrape all workshop links that the currently logged in user is subscribed to and writes the links to a file for the subscriber to mass subscribe to.
> Has to be the currently logged in user, due to Steam's privacy settings.

### The ideal audience is a group of friends attempting to synchronize workshop packages, such as for Garry's Mod. The hosting user would rip their workshop subscriptions and share the text file for the other friends to subscribe to using the respective Python3 scripts.
---
## Requirements
### Python 3 (Tested on 3.10.4, make sure it is added onto PATH)
### The following Python Modules: selenium

### To install selenium, type the following command into command prompt.
```bash
pip install selenium 
```

### You will also need a Chrome Driver for Selenium and Chrome
> For more details: [https://selenium-python.readthedocs.io/installation.html]
---
## Steps 
### 1. Install Python from official website [https://www.python.org/downloads/]
### 2. Install Selenium: Enter pip install selenium in command prompt
### 3. Download respective driver and place it in the directory where the scripts and output folder will be (or in PATH).
### 4. Run the main.py file (either by clicking the file, or in terminal
### 5. Enter the path to the folder containing the chromedriver
### 6. Login to Steam in the new Chrome window that opens.
### 7. Select your option in the command prompt and refer to that particular section below for more info (1 for ripping, 2 for subbing, 3 to exit)

## Ripping
### Enter the URL to your workshop subscriptions for the particular title.
### Enter the number of addons you have (this allows the program to know how many pages worth of addons you have)
### The created "links.txt" file should be in a subfolder label links in the same directory as the provided before.

## Subscribing
### Ensure that there a subfolder labelled "links" which contains a properly formatted links.txt file.
### The program should automatically go to each link and subscribe if it is not already.

> Any output with a starting with [+] or [-] are status updates by the program.
> Plain text is usually displayed when asking for input from the user
> Anything else such as random messages like "[22300:26892:0424/133641.441:ERROR:gpu_init.cc(446)] Passthrough is not supported, GL is disabled" can be ignored.
---
### Notes
#### If you use a different browser instead of Chrome, you will have to change all Chrome references to accomodate your driver.
#### Your driver will also need to be set on PATH (refer to the selenium documentation for more info), unless given a proper location in the program.
#### If the program ripping process finished almost instantly, check and ensure your profile's workshop link was enter correctly.
#### The subscriber assumes that the links file will be named links.txt inside of a links directory (similarly to how it is output during the ripper process) and will not work correctly unless the program is adjusted for other naming conventions.
#### You may have to use the subscribe function multiple times, there is a potential chance that a page may or may not subscribe.
