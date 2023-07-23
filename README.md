# ScryFetcher README.md
A script to retrieve bulk data from scryfall.com via their API and then writing it in a csv file.
## Current version: v1.1

## Usage for v1.x:
1. Make sure you have the newest version of Python 3 installed (tested on python 3.11)
2. Change the path name in scryfallwrite.py to where you are storing your database (line 16)
3. Change the table name in scryfallwrite.py to what table you want to read from
### Dislcaimer: At the current stage the csv will only be filled if there are matching values in the specified columns during the loop. For now this is unique to what I have in my database.
4. Run scrywrite.py in the command line: >python .\scrywrite.py
5. After it finishes executing, scryfallbulk.csv now contains the requested values

For 2.0 I will add a database writing functionality as well as an executable for ease of use