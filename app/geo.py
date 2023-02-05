from geopy import Yandex
from dotenv import load_dotenv
import os


load_dotenv()


def get_longitude(place):
    location = Yandex(api_key=os.getenv('YANDEX_API_KEY')).geocode(place)
    return location.longitude


def get_latitude(place):
    location = Yandex(api_key=os.getenv('YANDEX_API_KEY')).geocode(place)
    return location.latitude
