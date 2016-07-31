#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import twitter
import datetime

#Initialize some variables.
changed = False
simple_status = "up"

#Code from Reddit to get the PoGo status.
#https://gist.github.com/donniebishop/a1cc00d9e1d6751a6f6ee64ca5d3e24f
poke_url = "http://cmmcd.com/PokemonGo/"
request_it = requests.get(poke_url)
try:
    import lxml
    soup = BeautifulSoup(request_it.text, "lxml")
except ImportError:
    soup = BeautifulSoup(request_it.text, "html.parser")

status = soup.body.header.h2.font.text

if status == "Unstable!":
    simple_status = "unstable"
elif status == "Offline!":
    simple_status = "down"
else:
    simple_status = "up"

#Read the file.
with open("/path/to/file/statusdb.txt", "r") as file_object:
    contents = file_object.read()
    #Figure out if there are changes.
    if contents.rstrip() != simple_status:
        changed = True
    else:
        changed = False

#Now update it if needed.
if changed:
    #First update the text file for next time.
    with open("/path/to/file/statusdb.txt", "w") as file_object:
        file_object.write(simple_status + "\n")

    #Now connect with Twitter.
    #More info on this setup at: https://python-twitter.readthedocs.io/en/latest/getting_started.html
    api = twitter.Api(consumer_key = "consumer_key",
        consumer_secret = "consumer_secret",
        access_token_key = "access_token_key",
        access_token_secret = "access_token_secret")

    #Parse the message details.
    if simple_status == "up":
        message = "Pokemon is a go! - " + datetime.datetime.now(datetime.timezone.utc).strftime("%Y:%m:%d %H:%M") + " UTC" 
    elif simple_status == "down":
        message = "Pokemon is a no go... - " + datetime.datetime.now(datetime.timezone.utc).strftime("%Y:%m:%d %H:%M") +  " UTC" 
    else:
        message = "Pokemon Go at your own risk. - " + datetime.datetime.now(datetime.timezone.utc).strftime("%Y:%m:%d %H:%M") +  " UTC"

    #Post to Twitter.
    status = api.PostUpdate(message)
