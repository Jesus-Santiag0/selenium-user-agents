import random
from time import sleep
#Libraries needed for dynamic pages
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# selenium 4 (browser Firefox)
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Reading the .txt file, cleaning it up, and saving it to the user_agents list
r=open("user-agents.txt","r")
lines=r.readlines()
user_agents=[]
for line in lines:
	cleanline=line.strip()
	user_agents.append(cleanline)
r.close()


# Amazon links
urls=["https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A193870011&ref=nav_em__nav_desktop_sa_intl_computer_components_0_2_7_3","https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A1292110011&ref=nav_em__nav_desktop_sa_intl_data_storage_0_2_7_5","https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A11036071&ref=nav_em__nav_desktop_sa_intl_servers_0_2_7_13","https://www.amazon.com/b/ref=SHWN/?_encoding=UTF8&ie=UTF8&node=21217028011&ref_=cct_cg_SHnav2_4d1&pf_rd_p=0b4b41c4-3a43-4ea8-8624-5c61818e900b&pf_rd_r=0S2ARFKPF9TGRTCGNZ7B"]

for url in urls:
	# A user-agent is randomly chosen
	user_agent=random.choice(user_agents)
	# Selenium Heders
	opts=Options()
	opts.add_argument(f"User-Agent={user_agent}")
	opts.add_argument("--disable-search-engine-choice-screen")
	driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=opts)
	# visit the url
	driver.get(url)
	# Displays the user agent used
	print(f"User-Agent used: {user_agent}")
	sleep(1)
	driver.quit()