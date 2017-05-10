#!/usr/bin/env python 
from bs4 import *
import requests
import argparse 

parser = argparse.ArgumentParser() 

parser.add_argument("-l", "--location", action="store", help = "specify location as ag or marquis", default="ag", dest="loc") 

args=parser.parse_args()
if("ag" in args.loc.lower() ): 
  myUrl="http://www.usask.ca/culinaryservices/agriculture-menu.php"
else: 
  myUrl="http://www.usask.ca/culinaryservices/marquis-menu.php"

#use the request package to make the request
menu = requests.get(myUrl)

#check that the request worked
#print(menu.text)

#use beautiful soup to parse the HTML available from the request object (menu) 
lunch = BeautifulSoup(menu.text, 'html.parser')

#print(lunch.get_text())
for i in lunch.find_all('p'): 
  if "University" not in i.text:
    print(i.text.encode('utf8'))
