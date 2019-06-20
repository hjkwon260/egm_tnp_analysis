import os, sys, json

print("####### combine scale factor json files for each Id ######")
json_list = []
current_dir = os.path.dirname(__file__)
era = sys.argv[1]
combined_filename = 'combined_eleIDSFs_'+era+'.json'

for (path, dir, files) in os.walk(current_dir+'/../../results/'): # or use absolute path
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.json':
            json_path = "%s/%s" % (path, filename)
            json_list.append(json_path)
           
if not json_list:
    print(" SF JSON files are not created... nothing to combine ")
    sys.exit(1)
if os.path.isfile(current_dir+'/../../'+combined_filename) == True:
    print(" Warning : combined JSON already exists... exit ")
    sys.exit(1)

json_combine = {}
for k in json_list:
	print(k)
	with open(k) as json_data:
		json_combine.update(json.load(json_data))

year = {}
year[era] = json_combine

with open(current_dir+'/../../'+combined_filename,'w') as f:
    json.dump(year, f, sort_keys = False, indent = 4)

