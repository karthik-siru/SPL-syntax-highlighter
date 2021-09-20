import requests
from bs4 import BeautifulSoup

ref = requests.get(url="https://exposnitc.github.io/support_tools-files/constants.html")

soup = BeautifulSoup(ref.content, features="html.parser")
constants = soup.find_all("td")
fh = open("spl_constants.txt", "w")

for i in range(len(constants)):
    if i%3 == 0:
       fh.write(constants[i].get_text())
       fh.write("|")
    i += 1 
      
fh.close()
