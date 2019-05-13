import glob
import json
alldata = []
allfiles = glob.glob("foggdata/*.json")
#print (allfiles)

for file in allfiles:
	foggfile = json.load(open (file))
#	alldata = alldata + foggfile ["records"]
	print (file)
	for record in foggfile['records']:
		harvard = {}
		if 'people' in record:
			harvard['people'] = record ["people"]
		if 'edition' in record:
			harvard['edition'] = record ["edition"]
		alldata.append(harvard)
json.dump (alldata, open ("finaldump.json", "w"))