from modules.library_item import LibraryItem
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.cd import Cd
from modules.book import Book
from modules.catalog import Catalog
import json

f = open('files/data.json')
data_json = json.load(f)

list_book = []
list_magazine = []
list_dvd = []
list_cd = []

for item in data_json:
    if item['source'] == 'book':
        list_book.append(Book(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            isbn = item['issbn'],
            authors = item['authors'],
            dds_number = item['dds_number']
        ))
    elif item['source'] == 'magazine':
        list_magazine.append(Magazine(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            volume = item['volume'],
            issue = item['issue']
        ))
    elif item['source'] == 'dvd':
        list_dvd.append(Dvd(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            actors = item['actors'],
            director = item['directors'],
            genre = item['genre']
        ))
    elif item['source'] == 'cd':
        list_cd.append(Cd(
            title = item['title'],
            subject = item['subject'],
            upc = item['upc'],
            artist = item['artist'],
        ))

catalog_all = [list_book, list_magazine, list_dvd, list_cd]

input_search = 'test'
results = Catalog(catalog_all).search(input_search)

print('=====| Result |=====')
for index, result in enumerate(results):
    print(f'Result ke-{index+1} | {result}')
    
