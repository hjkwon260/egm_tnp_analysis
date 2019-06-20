import os, sys, json

print("####### combine all years of SF json files ######")

json_list = ['combined_eleIDSFs_2018-Prompt.json', 'combined_eleIDSFs_2017-Nov17ReReco.json', 'combined_eleIDSFs_2016-Legacy.json']

json_combine = {}
for k in json_list:
	print(k)
	with open(k) as json_data:
		json_combine.update(json.load(json_data))

with open('combined_eleIDSFs_All_years.json','w') as f:
    json.dump(json_combine, f, sort_keys = False, indent = 4)