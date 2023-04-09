from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

# URL to scrape
url = 'https://www.example.com'

# Fetch the content from the URL
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Extract the data
data = []
for row in soup.find_all('tr'):
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    data.append(cols)

# Convert data to a numpy array
data_array = np.array(data)

# Create a pandas dataframe from the numpy array
df = pd.DataFrame(data_array)

# Export the data to a CSV file
df.to_csv('output.csv', index=False)
