import requests
from bs4 import BeautifulSoup


def totalcases(url, country):

    request = requests.get(url)
    s = BeautifulSoup(request.text, "html.parser")
    data = s.find_all("div", class_="maincounter-number")
    data_active = s.find_all("div", class_="number-table-main")
    print()
    print("Total Cases in %s: %s" % (country, data[0].text.strip()))
    print("Total Deaths in %s: %s" % (country, data[1].text.strip()))
    print("Total recovered in %s: %s" % (country, data[2].text.strip()))
    print("Active Cases in %s: %s" % (country, data_active[0].text.strip()))


totalcases("https://www.worldometers.info/coronavirus/", "World")
totalcases("https://www.worldometers.info/coronavirus/country/india/", "India")

input("Press 'ENTER' to exit")
