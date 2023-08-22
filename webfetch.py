import requests
import json

class API_Call:
     def call_func():
          # declare api endpoint variable
          scryurl = "https://api.scryfall.com/bulk-data/all-cards"

          # get request to scryfall api endpoint (url)
          response = requests.get(scryurl)
          # print status code of response
          print (response)

          # create new json in writing mode with utf-8 encoding
          outf = open("responsecontent.json", "w", encoding="utf-8")
          print("responsecontent.json has been created")
          # write response text into json
          outf.write(response.text)
          # close json
          outf.close()
          print("responsecontent.json has finished writing")

          # open newly created json for reading
          resjData = open("./responsecontent.json", "r", encoding="utf-8")

          # load json in variable
          resData = json.load(resjData)
          print("responsecontent.json was loaded")
          # retrieve download uri from json
          bulkUrl = resData["download_uri"]
          # get request to download uri
          bulkResponse = requests.get(bulkUrl)
          # print status code of response
          print(bulkResponse)

          # write text content into new json
          bulkjson = open("bulkdata.json", "w", encoding="utf-8")
          print("bulkdata.json has been created")
          bulkjson.write(bulkResponse.text)
          bulkjson.close()
          resjData.close()
          print("bulkdata.json has finished writing")

          return True