from webfetch import API_Call
import os
import csv
import pyodbc
import pathlib
import json

class csvWriter:
     def dbinput():
          print("Please enter your database location (as path): ")
          db_input = input()
          return db_input
     
     def tbinput():
          print("Please enter the name of the table you want to take data from: ")
          tb_input = input()
          return tb_input
     
     def tbinput_col():
          print("Please enter the name of the column you want to write the price data into: ")
          tbinput_col = input()
          return tbinput_col
     
     def locJson_check():
          if os.path.isfile("./fileloc.json"):
               return
          else:
               #inputs for file locations
               db_locw = csvWriter.dbinput()
               tb_locw = csvWriter.tbinput()
               tb_col = csvWriter.tbinput_col()
               #json list layout
               dicLoc = {"db_loc":db_locw, "tb_loc":tb_locw, "tb_col":tb_col}
               #saves data to json format
               json_loc = json.dumps(dicLoc, indent=3)
               #write into json file
               with open("./fileloc.json", "w") as outfile:
                    outfile.write(json_loc)                   
               #closes file and ends function
               outfile.close()
               return

     def scrywrite():
          csvWriter.locJson_check()
          json_locFile = open("./fileloc.json", "r")
          fileContent = json.load(json_locFile)

          db_loc = fileContent.get("db_loc")
          tb_loc = fileContent.get("tb_loc")
          
          dbFile = pathlib.Path(r"%s" % db_loc)

          # connect access database with script
          db = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                                     r"DBQ=%s" % dbFile)
          cursor = db.cursor()
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

          db.close()
          jData.close()
          # os.remove("D:/Coding/VSCodeStuff/ScryFetcher/bulkdata.json")
          # os.remove("D:/Coding/VSCodeStuff/ScryFetcher/responsecontent.json")
          print("Deleted json files")

#csvWriter.scrywrite()