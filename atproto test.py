# simple python script that takes the latest entry on your status.cafe and posts it to bluesky using the atproto api
# usage: replace placeholders in feed and client.login with corresponding information. then every time you want to upload your status.cafe to bluesky, simply run this script!
# a future iteration aims to make this more automated, so you wont have to think about it

from atproto import Client
import feedparser
feed = feedparser.parse("https://status.cafe/users/your statuscafe username.atom")
entry = feed.entries[0]
postentry = entry.summary
print('Latest entry on status cafe:', postentry)

client = Client()
client.login('your handle', 'your password')

post = client.send_post("[status.cafe] " + postentry)
