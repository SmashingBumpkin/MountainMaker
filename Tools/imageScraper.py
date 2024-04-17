import cv2
import numpy as np
from urllib.request import urlopen
import cv2
from cv2.typing import MatLike
from ImageTools import resize_and_center_crop_image

import xml.etree.ElementTree as ET
import flickrapi

api_key = "2decb6fe3a5c7762639cfb9802e7b4da"
api_secret = "c81ea6e8a8793c82"

flickr = flickrapi.FlickrAPI(api_key, api_secret)
flickr.authenticate_via_browser(perms="read")

flickr = flickrapi.FlickrAPI(api_key, api_secret, format="etree")
url_type = "url_n"
results = flickr.photos.search(
    page="26",
    tag_mode="all",
    tags="mountain, alps, snow",
    extras=url_type,
    per_page=6,
    sort="relevance",
    geo_context="0",
    content_types="0",
)


def GetImage(url: str) -> MatLike:

    resp = urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")

    return image


i = 0
for data in results[0]:
    title = data.get("title")
    url = data.get(url_type)
    if url != None:
        image_raw = GetImage(url)
        # decode the image with color
        image = cv2.imdecode(image_raw, cv2.IMREAD_COLOR)

        # image processing?
        cv2.imshow("img", image)
        key = cv2.waitKey(0)
        # Check key pressed
        if key == 2490368:  # Up arrow key
            print("Confirmed")
            # Perform actions for confirmation
            cv2.imwrite(f"testdata/raw/Mountain-{str(i)}.jpg", image)
            cv2.imwrite(
                f"testdata/scaled/Mountain-{str(i)}.jpg",
                resize_and_center_crop_image(image, 280, 190),
            )
            i += 1

        elif key == 2621440:  # Down arrow key
            print("Denied")
            # Perform actions for denial
        else:
            print("No action taken")
