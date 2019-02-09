# Python script to display a list of accounts which you are following but aren't following you back

import requests
from bs4 import BeautifulSoup
import time

class insta:
    def __init__(self):
        self.results = []

    def getFollowers(self, username):
        followers = []
        link = "https://www.instagram.com/" +username+ "/followers/"
        url = requests.get(link)
        soup = BeautifulSoup(url.text, "html.parser")
        time.sleep(1)
        aTags = soup.find_all('a', class_ = "FPmhX notranslate _0imsa ")
        for tag in aTags:
            followers.append(tag.text.strip())
        return followers

    def getFollowing(self, username):
        following = []
        link = "https://www.instagram.com/" +username+ "/following/"
        url = requests.get(link)
        soup = BeautifulSoup(url.text, "html.parser")
        time.sleep(1)
        aTags = soup.find_all('a', class_ = "FPmhX notranslate _0imsa ")
        for tag in aTags:
            following.append(tag.text.strip())
        return following  

    def getResults(self, username):
        followers = self.getFollowers(username)
        following = self.getFollowing(username)
        self.results = list(set(following)-set(followers))
        print ("List of Accounts which haven't followed you back")
        print ("================================================")
        for acc in self.results:
            print (acc)
        print ("================================================")

i = insta()
user = input("Enter a valid Instagram username: ")
followers = i.getFollowers(user)
print (followers)