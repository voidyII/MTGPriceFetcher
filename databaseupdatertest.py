import pyodbc

def main():
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                          r"DBQ=D:/MTGCollection/MTGCollection.accdb")
    cursor = conn.cursor()
    cursor.execute("select * from CompleteCollection")

    for row in cursor.fetchall():
        sCode = row[1]
        cNum = row[4]
        cName = row[5]
        cFoil = row[9]
        if cFoil == "yes":
            cFoil = True
        else:
            cFoil = False
        cCond = row[13]
        print (sCode, cNum, cName, cFoil, cCond)

if __name__ == "__main__":
    main()