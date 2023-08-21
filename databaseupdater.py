import pyodbc
import pathlib
from localwrite import csvWriter

def datareader():
    file_loc = open("./fileloc.txt", "r+")
    fileContent = file_loc.readlines()

    if fileContent[3] == None:
        print("Please enter column specifier to add prices. If you want the complete data to be replaced, leave blank.")
        tb_col = input()
        file_loc.write(tb_col+"\n")
    else: 
        db_loc = fileContent[0]
        tb_loc = fileContent[1]
        tb_colLoc = fileContent[3]

    dbFile = pathlib.Path(r"%s" % db_loc)

    tb_col2 = "{tb_loc}.{tb_colLoc}"

    # connect access database with script
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                              r"DBQ=%s" % dbFile)
    cursor = conn.cursor()
    print("database connection established")

    for row in cursor.fetchall():
        # convert float value in database to string
        if row[4] != None:
            flV = row[4]
        else: flV = 0
        flV = int(flV)
        flV = str(flV)
        # # if card is foil, write eur_foil in csv
        # if item.get("collector_number") == flV and item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower() and row[9] == "yes":
        #     writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), pItem.get("eur_foil")])
        # #if card is not a foil, write eur in csv
        # if item.get("collector_number") == flV and item.get("name") == row[5] and item.get("lang") == row[14] and item.get("set") == row[1].lower() and row[9] == "no":
        #         writer.writerow([item.get("set"), item.get("collector_number"), item.get("name"), pItem.get("eur")])

    writeText = "Insert into %s (F17) values"


if __name__ == "__main__":
    datareader()