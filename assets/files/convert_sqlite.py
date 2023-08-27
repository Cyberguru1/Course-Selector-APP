#!/usr/bin/env python
"""converting the merged json file to sqlite databse"""

import sqlite3
import json


#   {
#     "id": "25681",
#     "title": "FORESTRY TECHNOLOGY",
#     "de_requirements": "<p>NIL</p>",
#     "utme_requirements": "<p><span>Five (5)\r\nSSC credit passes in Mathematics, Physics and Chemistry and any two (2) subjects\r\nfrom:</span></p><p><span>Biology/Agricultural\r\nScience </span></p><p><span>Technical\r\nDrawing,</span></p><p><span>Basic\r\nElectronics/Basic Electricity,</span></p><p><span>Auto\r\nMechanics,</span></p><p><span>Metal\r\nWork, Woodwork for Civil Engineering Technology,</span></p><p><span>Further\r\nMathematics</span></p><p><span>English\r\nLanguage, Geography,</span></p><p><span>Economics/Commerce.</span></p><p><span>For Marine\r\nEngineering and Industrial Safety &amp; Environmental Engineering. 'O' Level\r\npass in Biology is required.</span></p><p>\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n</p><p><span>'O' Level\r\ncredit pass in English Language is required.</span></p>",
#     "subjects": "<p><span>Mathematics\r\nand any two (2) of Chemistry, Physics or Technical Drawing.</span></p><p>\r\n\r\n</p><p><span>&nbsp;</span></p>",
#     "institutions_list": "FEDCO-MAID",
#     "InstType": "ND",
#     "SubInstType": "FEDERAL MONOTECHNICS",
#     "UniName": "FEDERAL COLLEGE OF FOREST RESOURCES MANAGEMENT, MAIDUGURI, BORNO STATE",
#     "ID": 964
#   }

with open("merged_data.json", 'r') as file:
    data = json.load(file)

conn = sqlite3.connect("ibass_database.db")

cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS Entities (
    title TEXT,
    de_requirements TEXT,
    utme_requirements  TEXT,
    subjects TEXT,
    InstType  TEXT,
    SubInstType TEXT,
    UniName TEXT,
    ID INTEGER
    )
""")
               
i = 0  

for entry in data:
    try:
       title = entry['title']
       de_requirements = entry['de_requirements']
       utme_requirements = entry['utme_requirements']
       subjects = entry['subjects']
       InstType = entry['InstType']
       SubInstType = entry['SubInstType']
       UniName = entry['UniName']
       ID = entry['ID']
    except:
        de_requirements = "None"
        utme_requirements = "None"
        subjects = "None"
        title = "None"
        i += 1

    cursor.execute("""
        INSERT INTO Entities (
            title, 
            de_requirements, 
            utme_requirements,
            subjects,
            InstType,
            SubInstType,
            UniName,
            ID
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (title,
              de_requirements,
              utme_requirements,
              subjects,
              InstType,
              SubInstType,
              UniName,
              ID
            )
        )

conn.commit()
conn.close()
print(i)