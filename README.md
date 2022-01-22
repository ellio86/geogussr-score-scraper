# Geoguessr Score Scraper
**Paste in your results link to the script and it will scrape the data from the page and automatically add it to a spreadsheet**

The scraper uses the selenium chrome driver to open a browser and find the appropriate data. The script will also create new sheets
for any game that does not yet have any times stored. 

Note: you can specify what sheet to use as an argument in the command line.
`python score-scraper.py my_spreadsheet.xlsx`

The default sheet is 'Geoguessr.xlsx'.