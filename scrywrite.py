from scryfallfetch import API_Call
import csv
import pyodbc
import json

def scrywrite():
     call_response = API_Call.call_func()
     if call_response == True:
          # open locally stored .json file and load into variable
          jData = open("./bulkdata.json", encoding="utf-8")
          data = json.load(jData)
          print("bulkdata.json has been loaded")

          # connect access database with script
          conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                                r"DBQ=[insert/path/to/database]")
          cursor = conn.cursor()
          cursor.execute("select * from [insert_table_name]")
          print("database connection established")

          # open csv file and create writer variable
          file = open("./scryfallbulk.csv", "w", encoding = "UTF-8", newline = "")
          writer = csv.writer(file)
          print("scryfallbulk.csv ready for writing")

          # compare values from database with json
          print("starting writing process, duration varies")
          for row in cursor.fetchall():
               for item in data:
                    # convert float value in database to string
                    if row[4] != None:
                         flV = row[4]
                    else: flV = 0
                    flV = int(flV)
                    flV = str(flV)
                    # variable to access values in "prices"
                    pItem = item.get("prices")
                    # if card is foil, write eur_foil in csv
                    if item.get("collector_number") == flV and item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower() and row[9] == "yes":
                         writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), pItem.get("eur_foil")])
                    #if card is not a foil, write eur in csv
                    if item.get("collector_number") == flV and item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower() and row[9] == "no":
                         writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), pItem.get("eur")])
          print("finished writing")

scrywrite()