# status.cafe to bluesky
Simple python script that uploads the latest entry in a status.cafe (ie, your status.cafe) atom feed to bluesky.

currently, you need to manually run the script for this to actually do anything. 
in a future iteration i may make this into a more automated thing, so that you wont even have to think about it!

## requirements
have python installed on your computer i think...

python libraries
---
you may need some python libs to make this actually work. fortunately installing these is easy:

1. open your terminal
2. type in the following:
   ```
   pip install atproto
   pip install feedparser
   ```
3. breathe air or something i dunno

## how to use
1. replace placeholder text with your own information
- your status.cafe username goes into "your statuscafe username",
- your bluesky handle goes into "your handle"
- your password goes into "your password"
2. run the script on your computer

## to do
- figure out how to make links parse out correctly for bsky posts instead of it being spit out as a raw html `<a></a>`
- make process more automated, and in turn convinient, by possibly making a browser extention (i think there was an existing one that you can have custom scripts run for certain websites), or hell, just talking with the status.cafe devs on how to officially implement it into the thingy (it most likely will be the former)
