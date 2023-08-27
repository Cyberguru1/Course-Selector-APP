#!/usr/bin/env python
""" merge all the json data into one"""

import json
import os


json_dir = '/home/cyberguru/Documents/project/course_selector/assets/modded'
output_file = "merged_data.json"
merged_data = []

for filename in os.listdir(json_dir):
    if filename.endswith("_mod.json"):
        file_path = os.path.join(json_dir, filename)
        print(file_path)

        with open(file_path, 'r') as file:
            data = json.load(file)
            merged_data.extend(data)

    with open(output_file, "w") as output:
        json.dump(merged_data, output, indent=2)


# with open("merged_data.json", 'r') as f:
#     data = json.load(f)



# print(type(data))
# print(len(data))