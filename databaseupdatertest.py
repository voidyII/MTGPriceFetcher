import pyodbc

def main():
    conn = pyodbc.connect(r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
                          r"DBQ=D:/MTGCollection/MTGCollection.accdb")
    cursor = conn.cursor()
    cursor.execute("select * from CompleteCollection")

    for row in cursor.fetchall():
        data = row[1], row[4], row[5], row[9], row[13]
        print (data)

if __name__ == "__main__":
    main()