Scraping tool project for cvbankas.lt using Camoufox and Parsel.

scrape_discovery.py: Iterates through all pages on CV Bankas and saves the HTML source code into the /htmls folder. It navigates by incrementing the page number in the URL; the process terminates when a page threshold is exceeded (CV Bankas redirects to the first page if the limit is passed).

parse_discovery.py: Scans the /htmls folder, parses the collected HTML files, and extracts all unique job advertisement URLs into a links.txt file.

scrape.py: Reads links.txt and visits each individual job URL, saving the resulting HTML files into the /jobhtmls folder.

parse.py: Processes every HTML file in the /jobhtmls directory to extract structured data (such as ID, URL, job title, and location). The extracted data for each advertisement is then stored as an individual JSON file in the /jsons directory.

schema.sql: Initializes the required schema and creates a table within the PostgreSQL database.

fill_db.py: Iterates through the /jsons directory and populates the PostgreSQL table with the data from each JSON file.

You can run program with cli:

poetry run cvb "command"

available commands: 

"scrape-discovery", "scrape", "parse-discovery", "parse/init-db"