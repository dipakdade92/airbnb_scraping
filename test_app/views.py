from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import time
import requests
import re
import csv
from test_app.models import ScrapedData, Rating_field


def get_scraped_data(requeset):

    with open("csv_file.csv", "w") as f:
        writer = csv.writer(f)
        urls_list = [
            {
                "Springdale, Arkansas, United States": "https://www.airbnb.co.in/s/Europe/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&adults=1&date_picker_type=calendar&checkin=2022-10-15&checkout=2022-11-16&source=structured_search_input_header&search_type=search_query&query=Springdale%2C%20Arkansas%2C%20United%20States&price_filter_num_nights=32"
            },
            {
                "Fayetteville, Arkansas, United States": "https://www.airbnb.co.in/s/Europe/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&adults=1&date_picker_type=calendar&checkin=2022-10-15&checkout=2022-11-16&source=structured_search_input_header&search_type=search_query&query=Fayetteville%2C%20Arkansas%2C%20United%20States&price_filter_num_nights=32"
            },
            {
                "Rogers, Arkansas, United States": "https://www.airbnb.co.in/s/Europe/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&price_filter_input_type=0&adults=1&date_picker_type=calendar&checkin=2022-10-15&checkout=2022-11-16&source=structured_search_input_header&search_type=search_query&query=Rogers%2C%20Arkansas%2C%20United%20States&price_filter_num_nights=32"
            },
        ]
        data = [
            "city",
            "lat",
            "lng",
            "country",
            "beds",
            "bathroom",
            "listing_name",
            "listing_id",
            "guest",
            "review",
            "cleanliness",
            "accuracy",
            "communication",
            "location",
            "check_in",
        ]
        writer.writerow(data)
        writer.writerow([])
        for obj in urls_list:
            dict_key = [*obj][0]
            dict_value = obj[dict_key]
            writer.writerow([])
            writer.writerow([])
            writer.writerow(dict_key)
            get_listing_view(dict_value, writer)
    return HttpResponse("Csv created")


def get_listing_view(url, writer):
    response = requests.get(url)
    time.sleep(5)
    soup1 = BeautifulSoup(response.content, "lxml")
    for card in soup1.select('div[class="c4mnd7m dir dir-ltr"]'):
        detail_page_url = card.select_one('a[class="ln2bl2p dir dir-ltr"]')["href"]
        r = requests.get("https://www.airbnb.co.in/" + detail_page_url)
        soup = BeautifulSoup(r.content, "lxml")
        time.sleep(5)
        country = soup.select('span[class="_9xiloll"]')[0].text.split(",")[0]
        p_lat = re.compile(r'"lat":([-0-9.]+),')
        p_lng = re.compile(r'"lng":([-0-9.]+),')
        lat = p_lat.findall(r.text)[0]
        lng = p_lng.findall(r.text)[0]
        city = soup.select('span[class="_9xiloll"]')[0].text.split(",")[0]
        country = soup.select('span[class="_9xiloll"]')[0].text.split(",")[0]
        img = soup.find("img")["src"]
        try:
            ratting = soup.select('span[class="_17p6nbba"]')[0].text
        except:
            ratting = ""
        review = soup.select('button[class="_11eqlma4"]')[0].text
        guest = soup("span")[22].text
        bathroom = soup("span")[37].text
        beds = soup("span")[32].text
        listing_id = detail_page_url[7:15]
        listing_name = soup.select('h1[class="_fecoyn4"]')[0].text
       
        cleanliness = accuracy = communication = location = check_in = ""
        if len(soup.select('span[class="_4oybiu"]')) > 0:
            cleanliness = soup.select('span[class="_4oybiu"]')[0].text
            accuracy = soup.select('span[class="_4oybiu"]')[1].text
            communication = soup.select('span[class="_4oybiu"]')[2].text
            location = soup.select('span[class="_4oybiu"]')[3].text
            check_in = soup.select('span[class="_4oybiu"]')[4].text

        data = [
            city,
            lat,
            lng,
            country,
            beds,
            bathroom,
            listing_name,
            listing_id,
            guest,
            review,
            cleanliness,
            accuracy,
            communication,
            location,
            check_in,
            ratting,
        ]
        writer.writerow(data)
        ratings_obj = Rating_field.objects.create(
            accuracy=accuracy,
            cleanliness=cleanliness,
            communication=communication,
            location=location,
            checkIn=check_in,
        )
        ScrapedData.objects.create(
            listing_id=listing_id,
            name_of_listing=listing_name,
            city=city,
            country=country,
            bathrooms=bathroom,
            beds=beds,
            latitude=lat,
            longitude=lng,
            picture_url=img,
            ratings=ratings_obj,
        )
        print( city,lat,lng,country,beds,bathroom,listing_name,listing_id,guest,review,cleanliness,accuracy,communication,location,check_in,ratting)