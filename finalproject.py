import requests
import json


# r = requests.get('https://api.harvardartmuseums.org/object?apikey=346e2860-5eef-11e9-8221-d9fcf17d93ec&size=100&page=2000')

# print(r.text)

for page_count in range(1,2332):

	r = requests.get('https://api.harvardartmuseums.org/object?apikey=346e2860-5eef-11e9-8221-d9fcf17d93ec&size=100&page=' + str(page_count))
	

	json.dump(r.json(),open('foggdata/' + str(page_count) + '.json','w'), indent=2)
	print("Im on page number" + str(page_count))