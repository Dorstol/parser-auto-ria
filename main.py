from bs4 import BeautifulSoup
import requests
import json

page = 1


def write_json(new_data, filename="cars.json"):
    with open(filename, encoding="utf8") as json_file:
        data = json.load(json_file)

    data.append(new_data)

    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False)


while True:
    url = "https://auto.ria.com/car/used/?page=" + str(page)

    request = requests.get(url)
    soup = BeautifulSoup(request.content.decode("utf-8"), "html.parser")
    cars = soup.find_all("section", {"class": "ticket-item"})

    for car in cars:
        soldOut = car.find("i", {"class": "icon-sold-out"})
        if soldOut:
            continue
        carName = car.find("div", {"class": "head-ticket"}).text.strip()
        carLink = car.find("a", {"class": "address"}).get("href")
        carPrice = car.find("span", {"data-currency": "USD"}).text.replace(" ", "")
        carCityArr = car.find("li", {"class": "view-location"}).text.strip().split()[:-3]
        carCity = " ".join(carCityArr)
        carTransmission = car.select_one(".characteristic li:nth-of-type(4)").text.strip()
        carFuel = car.select_one(".characteristic li:nth-of-type(3)").text.strip()
        carRace = car.find("li", {"class": "js-race"}).text.strip()

        carObj = {
            "name": carName,
            "link": carLink,
            "price": carPrice,
            "city": carCity,
            "transmission": carTransmission,
            "fuel": carFuel,
            "race": carRace
        }

        write_json(carObj)
    page += 1
