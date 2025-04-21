# web-scraping-python

Amazon Product Scraper
This is a Python-based web scraping script that fetches product information from Amazon.de based on a user-input search query. It uses requests, BeautifulSoup, and pandas to extract, parse, and store product data.

Features:
Prompts the user to enter a product name.

Sends an HTTP request to Amazon’s search page.

Extracts the following data for each product: Title, Price, Rating, Number of Reviews. product Link.

Saves the scraped data to a .csv file named after the search term.

Automatically creates a local folder to store the results.

Technologies Used: Python 3, requests – for making HTTP requests, BeautifulSoup – for parsing HTML, pandas – for handling data and saving it as CSV, os – for file and folder operations
