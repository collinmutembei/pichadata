import os

import exifread
import pyperclip

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_FILENAME = '🏢.jpg'

image_path = os.path.join(SCRIPT_DIR, IMAGE_FILENAME)

# open image file
f = open(image_path, 'rb')

# exif tags
tags = exifread.process_file(f)


def image_location():
    """ returns the GPS coordinates of where the location was taken
    """

    # get gps data
    latitude = tags['GPS GPSLatitude'].values
    longitude = tags['GPS GPSLongitude'].values

    latitude_ref = tags['GPS GPSLatitudeRef'].values
    longitude_ref = tags['GPS GPSLongitudeRef'].values

    # create link to show location on google maps
    query = "{0}° {1}\' {2}\" {3} {4}° {5}\' {6}\" {7}".format(
                latitude[0],
                latitude[1],
                latitude[2].num / latitude[2].den,
                latitude_ref,
                longitude[0],
                longitude[1],
                longitude[2].num / longitude[2].den,
                longitude_ref,
        )

    return query


def copy_location_to_clipboard():
    pyperclip.copy(image_location())
    return "Location copied"

if __name__ == "__main__":
    copy_location_to_clipboard()
