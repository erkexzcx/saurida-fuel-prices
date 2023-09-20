#!/bin/python3

import requests
from bs4 import BeautifulSoup
import json

# Define headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Make a request to the website
r = requests.get("https://www.saurida.lt/kuro-kainos-degalinese/", headers=headers)
r.content

# Use the 'html.parser' to parse the page
soup = BeautifulSoup(r.content, 'html.parser')

# Find the table in the page
table = soup.find_all('table')[0]

# Find the headers
headers = [header.text.lower().strip() for header in table.find_all('th')]

# Find all the rows
rows = table.find_all('tr')

# Store the data
data = {}
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    # Make sure that the row has enough columns
    if len(cols) >= len(headers):
        # Use the first column as key, and the rest of the columns as values
        # Convert numeric values to float, "-" to 0
        data[cols[0]] = {headers[i]: float(cols[i].replace(',', '.')) if cols[i].replace('.','',1).replace(',', '', 1).isdigit() else (0 if cols[i] == '-' else cols[i]) for i in range(1, len(cols))}

# Print the data
print(json.dumps(data, indent=4, ensure_ascii=False))
