import requests
from lxml import html
import random
import json

# Reading the .txt file, cleaning it up, and saving it to the user_agents list
r=open("user-agents.txt","r")
lines=r.readlines()
user_agents=[]
for line in lines:
	cleanline=line.strip()
	user_agents.append(cleanline)
r.close()

# A user-agent is randomly chosen
user_agent=random.choice(user_agents) # type: ignore
headers={
	"user-agent":f"{user_agent}"
}

# Useragents.me is a website that provides an automatically updated list of the most recent and common user agents seen on the web across all types of devices, operating systems, and browsers. The data is always up-to-date and updated weekly.
url="https://useragents.me/"

# extract all information from the root
response=requests.get(url,headers=headers)
# Transforms it into HTML format
parser=html.fromstring(response.text)

# We get the section of the most common desktop user agents
list=parser.xpath("//div[@id='most-common-desktop-useragents-json-csv']//textarea/text()")[0]

# We transform it into JSON format to manipulate it
transformedlist=json.loads(list)
# we open the .txt file where we are going to store it
w=open("user-agents.txt","w")
for result in transformedlist:
	useragent=result["ua"]
	# we write the user agents
	w.write(f"{useragent}\n")
# cerramos el archivo .txt
w.close()