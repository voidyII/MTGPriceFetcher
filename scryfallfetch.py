import requests
import csv
import pyodbc
import json

def main():
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
               if item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower():
                    writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), item.get("prices")])

if __name__ == "__main__":
     main()



     # url = "https://data.scryfall.io/all-cards/all-cards-20230718213102.json"
     # response = requests.get(url)
     # print (response)

     # file = open("D:\MTGCollection\scryfallbulk.csv", "w", encoding = "UTF-8")
     # writer = csv.writer(file)
     # writer.writerows()

     # response.json()

     # print (response.text)