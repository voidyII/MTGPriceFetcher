import pyodbc
import pathlib
import json
import os
from localwrite import csvWriter

class dbUpdate:
    def fileloc_check():
        file_loc = open("./fileloc.json", "r+")
        fileContent = json.load(file_loc)

        if os.path.isfile("./fileloc.json"):
               return
        else: 
            print("fileloc.json could not be found. Program will now terminate")

    def dbConnect():
        csvWriter.scrywrite()
        # filelocs = dbUpdate.fileloc_check()
        # print(filelocs)
        # db_loc = filelocs[0]
        # tb_loc = filelocs[1]
        # tb_colLoc = filelocs[2]

        # dbFile = pathlib.Path(r"%s" % db_loc)

        # print(dbFile)

        # tb_col2 = f"{tb_loc}.{tb_colLoc}"
        
        # print(tb_col2)

        # connect access database with script
        # conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
        #                         r"DBQ=%s" % dbFile)
        # cursor = conn.cursor()
        # cursor.execute("select * from %s" % tb_col2)
        # print("database connection established")

        #for row in cursor.fetchall():
            # convert float value in database to string
            # if row[4] != None:
            #     flV = row[4]
            # else: flV = 0
            # flV = int(flV)
            # flV = str(flV)
            # # if card is foil, write eur_foil in csv
            # if item.get("collector_number") == flV and item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower() and row[9] == "yes":
            #     writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), pItem.get("eur_foil")])
            # #if card is not a foil, write eur in csv
            # if item.get("collector_number") == flV and item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower() and row[9] == "no":
            #         writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), pItem.get("eur")])

        #writeText = "Insert into %s values"

dbUpdate.dbConnect()