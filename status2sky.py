# simple python script that takes the latest entry on your status.cafe and posts it to bluesky using the atproto api
# usage: replace placeholders in feed and client.login with corresponding information. then every time you want to upload your status.cafe to bluesky, simply run this script!
# a future iteration aims to make this more automated, so you wont have to think about it

from atproto import Client
import feedparser
client = Client()

# important stuff
feed = feedparser.parse("https://status.cafe/users/username.atom") # replace "username" with your status.cafe username
client.login('handle', 'password') # replace handle and password with your bsky handle and password

entry = feed.entries[0]
postentry = entry.summary
pubdate = entry.published


print('Your last entry on status.cafe: "', postentry, '" ', "\nYou submitted it specifically on", entry.published)
yn = input("\nWould you like to post the above status to bluesky? (y/n) ")
if yn == "y":
    post = client.send_post("[status.cafe] " + postentry)
    print("\nPosted!")
elif yn == "n":
    print("\nAborted")
else:
    print("\nInvalid choice, presuming no.")
    print("Have a nice day!")




