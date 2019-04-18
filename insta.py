# Python script to display a list of accounts which you are following but aren't following you back

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import time

class insta:
    def __init__(self):
        self.results = [] # contains the final result showing difference between following and followers
        self.followers = [] # contains the usernames of profiles following you
        self.following = [] # contains the usernames of profiles you follow
        self.scroll_script = """function sleep(ms) {
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
        scroller()"""
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(0.5)

    def login (self, user, pw):
        # Enters login details 
        wait = WebDriverWait(self.browser,120)  
        username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        username.send_keys(user)
        password = self.browser.find_element_by_name("password")
        password.send_keys(pw)

        # Clicks login button
        login_button = self.browser.find_elements_by_tag_name("button")
        login_button[1].click() 

    def goToProfilePage(self):
        # clicks the username link to redirect to user's profile page
        wait = WebDriverWait(self.browser,120)
        # if notification alert pops up, clear it
        # if notifications are already ON in your account, then comment out the next 2 lines
        notify_alert = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='piCib']/div[3]/button[2]")))
        notify_alert.click()
        a_profile = wait.until(EC.presence_of_element_located((By.XPATH, "//section/div/div/div/div[2]/div/a")))
        a_profile.click()

    def getFollowers(self, followers):
        # to find the followers and create a list of them
        wait = WebDriverWait(self.browser,120)
        follower_but = wait.until(EC.presence_of_element_located((By.XPATH, "//header/section/ul/li[2]/a")))
        follower_but.click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='isgrP']")))
        self.browser.execute_script(self.scroll_script)
        time.sleep(followers/10+10)
        a_followers = self.browser.find_elements_by_xpath("//div/div/div/div/a")
        for elm in a_followers:
            if elm.text != '':
                self.followers.append(elm.text)
        # print(self.followers)
        close_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Close']")))
        close_btn.click()

    def getFollowing(self, following):
        # to find the accounts followed by user and create a list of them
        wait = WebDriverWait(self.browser,120)
        following_but = wait.until(EC.presence_of_element_located((By.XPATH, "//header/section/ul/li[3]/a")))
        following_but.click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='PZuss']")))
        self.browser.execute_script(self.scroll_script)
        time.sleep(following/10+10)
        a_following = self.browser.find_elements_by_xpath("//div/div/div/div/a")
        for elm in a_following:
            if elm.text != '':
                self.following.append(elm.text)
        # print(self.following)
        close_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@aria-label='Close']")))
        close_btn.click()

    def getResults(self):
        # finds the list of accounts which don't follow back the user
        self.results = list(set(self.following)-set(self.followers))
        print()
        print ("------------------------ Final results ------------------------")
        for i in range(len(self.results)):
            print (str(i+1) + ". " + self.results[i])
        print()

    def closeWindow(self):
        # close the browser window after completion
        self.browser.close()

# Make sure to turn off 2 step verification before starting the process   
u = input("Enter Instagram username: ")
try:
    p = getpass.getpass(prompt="Enter password for the above account: ")
except Exception as e:
    print("Error:",e)

followers = int(input("Enter the number of followers you have: "))
following = int(input("Enter the number of accounts you follow: "))

# Creating class object and callling necessary functions
i = insta()
i.login(u, p)
i.goToProfilePage()
i.getFollowers(followers)
i.getFollowing(following)
i.getResults()
i.closeWindow()