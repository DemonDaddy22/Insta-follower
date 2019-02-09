from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import time

u = input("Enter Instagram username: ")
try:
    p = getpass.getpass(prompt="Enter password for the above account: ")
except Exception as e:
    print("Error:",e)

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(0.5)

user = browser.find_element_by_name("username")
user.send_keys(u)

pw = browser.find_element_by_name("password")
pw.send_keys(p)

login_button = browser.find_elements_by_tag_name("button")
login_button[1].click()

wait = WebDriverWait(browser,120)
time.sleep(7)

prof = u.lower()
a_profile = browser.find_element_by_partial_link_text(prof)
a_profile.click()

time.sleep(7)
followers = browser.find_element_by_partial_link_text(" followers")
followers.click()

time.sleep(2)
f_box = browser.find_element_by_xpath("//div[@class='isgrP']")
browser.execute_script("""function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function scroller() {
    var divTag = document.getElementsByClassName('isgrP');
    var d = divTag[0];
    var newHeight = 0;
    while (true){
        newHeight += 50;
        d.scrollTo(0, newHeight);
        await sleep(100);
        if (newHeight >= d.scrollHeight){
            break;
        }
    }
}
scroller()""")

time.sleep(30)
a_followers = browser.find_elements_by_xpath("//div/div/div/div/a")
followers_list = []
for elm in a_followers:
    if elm.text != '':
        followers_list.append(elm.text)
print(followers_list)

time.sleep(2)
close_btn = browser.find_element_by_xpath("//span[@aria-label='Close']")
close_btn.click()

time.sleep(2)