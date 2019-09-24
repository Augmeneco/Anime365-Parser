#!/usr/bin/python3
import requests, re, json, sys, os

url = sys.argv[1]

index = requests.get(url).text
index = re.findall('videoFrame" src="(.*)" wi',index)[0]
index = requests.get(index).text
index = re.findall('data-sources="(.*)" data-alternative-sources',index)[0]
index = index.replace('&amp;','&').replace('&quot;','"')

video = json.loads(index)[0]['urls'][0]

os.system('firefox --new-tab "'+video+'"&')