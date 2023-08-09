from scryfetch import API_Call
import os
import csv
import pyodbc
import pathlib
import json

class databaseupdate:
     def dbinput():
          print("Please enter your database location (as path): ")
          db_input = input()
          return db_input
     
     def tbinput():
          print("Please enter the name of the table you want to take data from: ")
          tb_input = input()
          return tb_input

     def scrywrite():
          if os.path.isfile("./fileloc.txt"):
               file_loc = open("./fileloc.txt", "r")
               fileContent = file_loc.readlines()
          else:
               newFile_loc = open("./fileloc.txt", "w")
               db_locw = databaseupdate.dbinput()
               tb_locw = databaseupdate.tbinput()
               newFile_loc.write(db_locw+"\n")
               newFile_loc.write(tb_locw)
               newFile_loc = open("./fileloc.txt", "r")
               fileContent = newFile_loc.readlines()


          db_loc = fileContent[0]
          tb_loc = fileContent[1]
          
          dbFile = pathlib.Path(r"%s" % db_loc)

          # connect access database with script
          conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                                     r"DBQ=%s" % dbFile)
          cursor = conn.cursor()
          cursor.execute("select * from %s" % tb_loc)
          print("database connection established")
          
          call_response = API_Call.call_func()
          if call_response == True:
               # open locally stored .json file and load into variable
               jData = open("./bulkdata.json", encoding="utf-8")
               data = json.load(jData)
               print("bulkdata.json has been loaded")

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

databaseupdate.scrywrite()

os.remove("D:/Coding/VSCodeStuff/ScryFetcher/bulkdata.json")
os.remove("D:/Coding/VSCodeStuff/ScryFetcher/responsecontent.json")

print("Deleted json files")