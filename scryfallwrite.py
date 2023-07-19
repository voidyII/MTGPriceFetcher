from scryfallfetch import main
import csv
import pyodbc
import json

def scrywrite():
 # open locally stored .json file
     jData = open("D:/MTGCollection/all-cards-20230718092007.json", encoding="utf-8")

     # load data from file into variable
     data = json.load(jData)

     # connect access database with script
     conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                          r"DBQ=D:/MTGCollection/MTGCollection.accdb")
     cursor = conn.cursor()
     cursor.execute("select * from CompleteCollection")

     # open csv file and create writer variable
     file = open("D:\MTGCollection\scryfallbulk.csv", "w", encoding = "UTF-8", newline = "")
     writer = csv.writer(file)

     # compare values from database with json
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

if __name__ == "__scrywrite__":
     scrywrite()