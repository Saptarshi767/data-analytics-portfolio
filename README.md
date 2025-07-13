

<h1 align="center">🚀 Data Analytics Portfolio</h1>
<p align="center">
  <b>By Saptarshi Mahapatra — Data Analyst | Python | Power BI | Automation</b>
</p>

<p align="center">
  <a href="#projects"><img src="https://img.shields.io/badge/Projects-12+-blueviolet?style=for-the-badge"/></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Skills-Python%2C%20Power%20BI%2C%20Automation%2C%20EDA-orange?style=for-the-badge"/></a>
  <a href="#datasets"><img src="https://img.shields.io/badge/Datasets-4-green?style=for-the-badge"/></a>
  <a href="https://github.com/Saptarshi767"><img src="https://img.shields.io/badge/GitHub-Saptarshi767-black?style=for-the-badge&logo=github"/></a>
  <a href="https://www.linkedin.com/in/saptarshi-mahapatra-4a1108268"><img src="https://img.shields.io/badge/LinkedIn-saptarshi--mahapatra-blue?style=for-the-badge&logo=linkedin"/></a>
</p>

---

## 🌟 Overview

Welcome to my Data Analytics Portfolio! This repository showcases my expertise in data analysis, automation, web scraping, and dashboarding using Python and Power BI. Here, you'll find:
- Automated data collection scripts
- Interactive dashboards
- Real-world business datasets
- End-to-end analytics workflows
- Advanced web scraping projects

---

## 🧑‍💻 About Me

Hi! I'm **Saptarshi Mahapatra**, a passionate data analyst skilled in:
- Python scripting & automation
- Data wrangling & cleaning
- Power BI dashboarding
- Web scraping & data extraction
- Business insights & storytelling

> **Let's connect!** [LinkedIn](https://www.linkedin.com/in/saptarshi-mahapatra-4a1108268) | [GitHub](https://github.com/Saptarshi767)

---

## 📁 Projects & Dashboards

### 1. **Automated Data Collection & Web Scraping Scripts**

#### `main all india.py` & `main all india2.py`
- **Purpose:** Automate downloading and aggregating daily Excel reports from the Merit India portal for all India.
- **Tech:** Python, requests, pandas
- **Features:**
  - Fetches daily data for a date range
  - Appends and saves as a single Excel file
  - Fully automated, ready for analytics

#### `main rajasthan.py`, `main rajasthan2.py`, `main rajasthan2high.py`
- **Purpose:** Automate Rajasthan-specific data downloads, including Selenium-based browser automation for complex downloads.
- **Tech:** Python, requests, pandas, selenium
- **Features:**
  - Handles state-specific data
  - Robust error handling and automation
  - Saves clean, ready-to-analyze datasets

#### **About the Web Scraping Approach**
- **Requests-based scraping:** For simple downloads, scripts use the `requests` library to fetch data directly from APIs or download links, then process with `pandas`.
- **Selenium-based scraping:** For dynamic or protected sites, Selenium automates browser actions (clicks, downloads, waits for files) to extract data that can't be accessed via direct requests.
- **Data cleaning:** All scripts include steps to clean, merge, and save data in analysis-ready formats.
- **Automation:** Scripts are designed for batch processing, error handling, and can be scheduled for regular data updates.

### 🚩 Featured Web Scraping Project


#### 🛒 Amazon Product Price Tracker
<p align="center">
  <img src="https://logos-world.net/wp-content/uploads/2020/04/Amazon-Logo.png" alt="Amazon Logo" width="200"/>
</p>
- **Description:** Monitors prices, titles, and availability of selected Amazon products. Saves results to CSV and prints to console.
- **Tech:** Python, requests, BeautifulSoup, pandas
- **How it works:**
  1. Add your Amazon product URLs to the script.
  2. Run the script: `python webscrape_amazon_price_tracker.py`
  3. Results are saved to `amazon_price_sample.csv`.
- **Sample Output:**

```csv
url,title,price,availability
https://www.amazon.in/dp/B09V4MXBSN,Apple iPhone 13 (128GB) - Midnight,52999,In stock
https://www.amazon.in/dp/B0C9J8PVX5,Samsung Galaxy S23 5G (256GB) - Phantom Black,74999,In stock
```

### 🎬 IMDb Top 250 Movies Scraper
- **Description:** Scrapes the IMDb Top 250 movies list, extracting each movie's title, year, rating, and (optionally) genre.
- **Tech:** Python, requests, BeautifulSoup, pandas
- **How it works:**
  1. Run the script: `python webscrape_imdb_top250.py`
  2. Results are saved to `imdb_top250_sample.csv`.
- **Sample Output:**

```csv
title,year,rating,genre
The Shawshank Redemption,1994,9.3,N/A
The Godfather,1972,9.2,N/A
The Dark Knight,2008,9.0,N/A
The Godfather: Part II,1974,9.0,N/A
12 Angry Men,1957,9.0,N/A
```

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg" alt="IMDb Logo" width="120"/>
</p>

---

#### **Additional Web Scraping Projects**

##### 1. **Amazon Product Price Tracker**
- Scrapes product prices, ratings, and availability from Amazon for selected items.
- Sends daily email alerts when prices drop below a threshold.
- Tech: Python, BeautifulSoup, requests, smtplib.

##### 2. **Real Estate Listings Scraper**
- Extracts property details (price, location, features) from popular real estate websites.
- Aggregates data for market trend analysis and visualization.
- Tech: Python, Selenium, pandas.

##### 3. **News Sentiment Analyzer**
- Scrapes latest news headlines and articles from multiple news portals.
- Performs sentiment analysis to track public mood on key topics.
- Tech: Python, requests, BeautifulSoup, TextBlob.

##### 4. **Job Listings Aggregator**
- Collects job postings from sites like Indeed and LinkedIn.
- Analyzes demand for specific skills and roles over time.
- Tech: Python, Selenium, pandas, matplotlib.

##### 5. **Weather Data Collector**
- Scrapes daily weather data (temperature, humidity, forecast) from meteorological websites.
- Builds a local weather history database for trend analysis.
- Tech: Python, requests, pandas.

##### 6. **YouTube Channel Analytics Scraper**
- Extracts video stats (views, likes, comments) from YouTube channels.
- Tracks channel growth and engagement over time.
- Tech: Python, Selenium, YouTube Data API.

---

### 2. **Power BI Dashboards**

#### `HR ANALYTICS DASHBOARD.pbix`
- **Description:** Visualizes HR data, including attrition, satisfaction, demographics, and salary analysis.
- **Highlights:**
  - Employee attrition trends
  - Departmental analysis
  - Salary and satisfaction insights

#### `KrizPay Market Research.pbix`
- **Description:** Market research dashboard analyzing sales, customer demographics, and business trends.
- **Highlights:**
  - Sales by region and segment
  - Customer profiling
  - Market opportunity insights

#### `Ecommerce Dashboard.pbix`
- **Description:** E-commerce analytics dashboard covering orders, revenue, and customer insights.
- **Highlights:**
  - Order trends and seasonality
  - Top customers and locations
  - Revenue breakdowns

---

## 📊 Datasets

| File                  | Description                                      | Rows  |
|-----------------------|--------------------------------------------------|-------|
| `HR_Analytics.csv`    | HR data: employee demographics, attrition, etc.  | 1482  |
| `Orders.csv`          | E-commerce order data: ID, date, customer, city  | 502   |
| `Details.csv`         | Transactional details: amount, profit, category  | 1502  |
| `Details - Copy.csv`  | Duplicate/backup of Details.csv                  | 1502  |

---

## 🛠️ Skills & Tools

- **Languages:** Python (pandas, requests, selenium, BeautifulSoup)
- **Visualization:** Power BI
- **Data:** Excel, CSV, Web scraping
- **Automation:** End-to-end data pipelines
- **Business:** E-commerce, HR, Market Research

---

## 🚦 How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Saptarshi767/data-analytics-portfolio.git
   ```
2. **Explore Python scripts:**
   - Run scripts in your Python environment (see code comments for usage)
3. **Open Power BI dashboards:**
   - Use Power BI Desktop to open `.pbix` files
4. **Analyze datasets:**
   - All CSVs are ready for analysis in Excel, Python, or BI tools

---

## ✨ Screenshots

<p align="center">

  <img src="Screenshot 2025-07-11 114338.png" alt="Screenshot 1" width="60%"/>
  <img src="Screenshot 2025-07-11 114225.png" alt="Screenshot 2" width="60%"/>
  <img src="Screenshot 2025-07-11 114029.png" alt="Screenshot 3" width="60%"/>
</p>

---

## 📬 Contact

- **Email:** [saptarshimahapatra007@gmail.com](mailto:saptarshimahapatra007@gmail.com)
- **LinkedIn:** [Saptarshi Mahapatra](https://www.linkedin.com/in/saptarshi-mahapatra-4a1108268)
- **GitHub:** [Saptarshi767](https://github.com/Saptarshi767)

---

<p align="center">
  <b>Thank you for visiting my portfolio! ⭐️</b>
</p> 
