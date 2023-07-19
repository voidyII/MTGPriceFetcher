import requests
import json

def api_call():
     # declare api endpoint variable
     url = "https://api.scryfall.com/bulk-data/922288cb-4bef-45e1-bb30-0c2bd3d3534f"

     # get request to scryfall api endpoint (url)
     response = requests.get(url)
     # print status code of response
     print (response)

     outf = open("responsecontent.json", "w", encoding="utf-8")
     outf.write(response.text)
     outf.close()

     

     resjData = open("D:/Coding/VSCodeStuff/DataScraper/responsecontent.json", "r", encoding="utf-8")

     resData = json.load(resjData)
     print(resData)






api_call()