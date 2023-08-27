#!/usr/bin/env python3

import requests
import json
import os


json_dir = '/home/cyberguru/Documents/project/course_selector/assets'

done =  os.listdir(json_dir)

url = 'https://ibass.jamb.gov.ng/assets/content/courses-by-institution/{}.json'


# with open("brochure_schools.json", 'r') as f:
#     output = json.loads(f.read())

# ppy = dict()
# for instType in output:
#     ppy["InstType"] = instType["name"]
#     for inst in instType["children"]:
#         ppy["SubInstType"] = inst["name"]
#         i = 0
#         for subinst in inst["children"]:
#             ppy["UniName"] = subinst["name"]
#             ppy["ID"]      = subinst["id"]
#             id = subinst["id"]
#             if id not in skipped:
#                 print("skippimg ", id)
#                 continue
#             with open(f"{id}.json", 'w') as f:
#                 out = requests.get(url.format(id))
#                 if out.status_code == 200:
#                     js = json.loads(out.text)
#                     js = [ppy] + js
#                     f.write(json.dumps(js))
#                     print(subinst["name"], f"is done remaining: {len(inst['children']) - i} in {inst['name']}")
#                     i += 1
# print("all done !")


for filename in done:

    if filename.endswith(".json"):
        file_path = os.path.join(json_dir, filename)
        print("currently on :",filename)

        if filename.split('.')[0]+"_mod.json" in os.listdir(json_dir+"/modded"):
                     print(f"Skipped {filename}")
                     continue

        with open(file_path, "r") as file:
            try:
                  data = json.loads(file.read())
            except:
                  skipped.append(filename)
                  continue
            
            ppy = data[0]
            res = []

            if len(data) == 1:
                 res.append(ppy)

            for content in data[1:]:
                content.update(ppy)
                res.append(content)

            file_path = os.path.join(json_dir, filename.split(".")[0]+"_mod.json")

            with open(file_path, "w") as f:
                 f.write(json.dumps(res))
                 print(f"file {filename} done")
        
# print(skipped)