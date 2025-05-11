# OLX Car Cover Scraper

This repository contains a Python script to scrape listings for **car covers** on **OLX India** and store the results in both CSV and Excel formats. The script uses **Selenium** to automate web browsing, gather car cover listings, and extract relevant details such as price, location, and listing title.

## Table of Contents

- [Description](#Description)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Output](#output)
- [Results](#results)

## Description

This project is a web scraper that extracts **car cover** listings from **OLX India** using the search URL `www.olx.in/items/q-car-cover`. The script collects relevant details for each listing, such as:

- Listing Title
- Price
- Location
- Description
- URL to the listing

The results are saved in both **CSV** and **Excel** formats for easy analysis and viewing.

## Technologies Used

- **Python** – The programming language used to write the scraper script.
- **Selenium** – A tool for automating web browsers, used to navigate and scrape data from OLX pages.
- **Pandas** – Used to save the scraped data to CSV and Excel files.
- **WebDriver** – The browser driver required for Selenium (e.g., `geckodriver` for Firefox).

## Requirements

Before running the script, make sure you have the following installed:

- **Python 3.12.10**
- **Selenium**: Install via pip
  ```bash
  pip install selenium

## Setup and Installment
1) Clone the Repository:
   ```bash
   git clone https://github.com/your-username/OLX-Car-Cover-Scraper.git
   cd OLX-Car-Cover-Scraper
2) Install the required Python Libraries
   ```bash
   pip install selenium pandas
3) Download `GeckoDriver` for Firefox or `ChromeDriver` for Chrome

## Output
The script will:

  - Open a browser window (Firefox by default) and begin scraping listings from OLX.

  - Extract details such as the title, price, location, and description for each listing.

  - Save the results to olx_car_covers.csv and olx_car_covers.xlsx in the project directory.

## Results
The script will save the results in the following files:

  -`olx_car_covers.csv` – A CSV file containing the scraped data.

  -`olx_car_covers.xlsx` – An Excel file with the same data.

  -`olx_results.txt` – A simple text file with basic details about the listings.
