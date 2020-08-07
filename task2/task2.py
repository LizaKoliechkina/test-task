import argparse
import flickrapi
from secure_data import FLICKR_API_KEY, FLICKR_API_SECRET
from image_db import insert, images_db

KEY = FLICKR_API_KEY
SECRET = FLICKR_API_SECRET

FLICKR = flickrapi.FlickrAPI(KEY, SECRET, format='parsed-json')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", type=str, default=None, help="Keywords used to find images")
    parser.add_argument("-n", "--number", type=int, default=None, help="Number of images to download")
    args = parser.parse_args()

    photos = None
    if args.keyword and args.number:
        photos = FLICKR.photos.search(tags=args.keyword, per_page=args.number)
        for p in photos['photos']['photo']:
            insert(images_db, p['id'], p['owner'], p['server'])
    else:
        photos = FLICKR.photos.getRecent(per_page=100, page=1)
        for p in photos['photos']['photo']:
            insert(images_db, p['id'], p['owner'], p['server'])

        print(photos)

