from icrawler.builtin import BingImageCrawler
import cv2
import os

# we are building cats image detection that's why we put cat here
# if you want some other images then put that name in classes list
classes = ['flower']
number = 5
# here root directory is find your root directory there u will find
# new file name data in which all images are saved.
for c in classes:
    bing_crawler = BingImageCrawler(
        storage={'root_dir': 'C:/Users/Gabriel Heinzer/OneDrive/Programme, Elektronik und Projekte/Python/ImageRenameAgent/images/p'})
    bing_crawler.crawl(keyword=c, filters=None,
                       max_num=number, offset=0)

classes = ['NOT']
number = 5
# here root directory is find your root directory there u will find
# new file name data in which all images are saved.
for c in classes:
    bing_crawler = BingImageCrawler(
        storage={'root_dir': 'C:/Users/Gabriel Heinzer/OneDrive/Programme, Elektronik und Projekte/Python/ImageRenameAgent/images/n'})
    bing_crawler.crawl(keyword=c, filters=None,
                       max_num=number, offset=0)
