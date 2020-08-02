import requests
import shutil

from time import sleep

#settings
url = "https://thispersondoesnotexist.com/image"
delay = 5 #seconds


def download_face():
    response = requests.get(url, stream=True)
    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    return response


download_face()