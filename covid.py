import requests
from bs4 import BeautifulSoup
import argparse
from colorama import Fore

parser = argparse.ArgumentParser(description="Covid-19 News")
parser.add_argument('-c', "--country", action='store_true', dest="country", required="True", help="Specify a country name")
args = parser.parse_args()
country = args.country
country = country.lower()


def totalcases(url, country):
    country = country.upper()
    request = requests.get(url)
    s = BeautifulSoup(request.text, "html.parser")
    data = s.find_all("div", class_="maincounter-number")

    print()
    print("Total cases in %s: %s" % (country,Fore.RED + data[0].text.strip() + Fore.RESET))
    print("Total deaths in %s: %s" % (country, Fore.RED + data[1].text.strip() + Fore.RESET))
    print("Total recovered in %s: %s" % (country,Fore.RED + data[2].text.strip() + Fore.RESET))

if __name__ == "__main__":
    adress = "https://www.worldometers.info/coronavirus/country/" + country
    totalcases(adress,country)
