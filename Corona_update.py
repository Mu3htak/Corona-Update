import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
data = s.find_all("div", class_="maincounter-number")
data_active = s.find_all("div", class_="number-table-main")

print()
print("Total Cases :", data[0].text.strip())
print("Total Deaths :", data[1].text.strip())
print("Total recovered :", data[2].text.strip())
print("Active Cases :", data_active[0].text.strip())
print("Closed Cases :", data_active[1].text)


url_india = "https://www.worldometers.info/coronavirus/country/india/"
r1 = requests.get(url_india)
s1 = BeautifulSoup(r1.text, "html.parser")
india = s1.find_all("div", class_="maincounter-number")

print()
print("Cases in India :", india[0].text.strip())
print("Deaths in India :", india[1].text.strip())
print("Recovered in India :", india[2].text.strip())
print()

input("Press 'ENTER' to exit")

