# ScryFetcher README.md
A script to retrieve bulk data from scryfall.com via their API and then writing it in a csv file.
## Current version: v1.1.5
Progress Tracker: https://trello.com/b/p1AS9164/mtgpricefetcher-development-progress

## Usage for v1.1.3 and further:
1. Make sure you have the newest version of Python 3 installed (tested on python 3.11)
2. Run scrywrite.py in the command line: >python .\scrywrite.py
3. After it finishes executing, scryfallbulk.csv now contains the requested values

### Dislcaimer: At the current stage the csv will only be filled if there are matching values in the specified columns during the loop. For now this is unique to what I have in my database.

For 2.0 I will add a database writing functionality as well as an executable for ease of use.

I also plan on using either the TGCPlayer or Cardmarket API in the future. Unfortunately, either they don't accept applications at this time or the requirements are above of what I am currently doing at the moment. So for now I will have to use Scryfall's API (which is the most useful for adding card details, as price informations is not too reliable).

If you like what I'm doing and want to support my work, here's a link to my ko-fi: https://ko-fi.com/voidyii
Donations make the progress on this project go faster and also help motivating me to keep going. It means a lot! <3