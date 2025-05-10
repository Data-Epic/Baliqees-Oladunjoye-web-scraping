
#  Premier League 2024/2025 Data Web Scraping Pipeline

##  Overview
This project scrapes Premier League 2024/2025 season data (Final Table, Points per Game, Average Goals Scored per Match, Top Scorers, and Squad Goalkeeping stats) from [fbref.com](https://fbref.com), processes the data using pandas, and uploads the resulting dataframes into a Google Sheet using the GSpread API.

##  Project Structure
```
webscraping/
├── scraper.py               # Contains EPLScraper class for scraping and processing data
├── gsheet_utils.py          # Google Sheets connection and upload functions
├── main2.py                 # Main pipeline script
├── credentials.json         # Google Service Account credentials (not shared publicly)
├── README.md                # Documentation (this file)
└── requirements.txt         # List of required Python packages
```

##  Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Baliqees-Oladunjoye-web-scraping.git
   cd Baliqees-Oladunjoye-web-scraping
   ```

2. **Install Required Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Google Sheets API**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a project and enable **Google Sheets API** and **Google Drive API**
   - Create a Service Account and download the JSON credentials file
   - Save the JSON file in the project directory as `credentials.json`
   - Share your target Google Sheet with the Service Account email (from the JSON file)

4. **Run the Pipeline**
   ```bash
   python main.py
   ```

##  Features Scraped & Processed

- **Final Table** (MP, W, D, L, GF, GA, GD, Pts)
- **Points per Game (PPG)** (calculated from Final Table)
- **Average Goals per Match**
- **Top Scorers**
- **Squad Goalkeeping Statistics**

##  Known Limitations

- **Hardcoded URLs**: The scraper currently targets a specific URL pattern for the 2024/2025 season on fbref.com. If the site structure changes, selectors will need updating.
- **Single Season Data**: The scraper is built for one season at a time. It doesn’t support scraping historical or multiple seasons yet.
- **Google Sheets Limitations**:
  - Maximum of 5 million cells per spreadsheet.
  - Google Sheets API quota may be exceeded if run excessively.
- **No Retry Handling**: Retry handling is currently unnecessary since data is scraped from local HTML files. If future updates involve live web scraping from URLs, a retry mechanism should be implemented to handle potential network errors or site restrictions.

##  Areas for Future Improvement

- **Automate URL Updates**: Dynamically detect and use the latest season's URL from the site homepage.
- **Add Logging & Error Handling**: Implement logging and robust try-except blocks.
- **Retry Logic for Network Failures**: Integrate retry mechanisms for failed web requests.
- **Pagination/Multiple Seasons Support**
- **Schedule Regular Runs**: Use a task scheduler (like cron jobs or Windows Task Scheduler) or cloud functions to automate daily/weekly scraping.
- **Data Visualization Dashboard**: Build a live dashboard using Streamlit or Looker Studio connected to the Google Sheet.

##  Requirements

See `requirements.txt` for all dependencies:

Example:
```
pandas
beautifulsoup4
requests
gspread
oauth2client
```

##  Author

Baliqees Oladunjoye 
