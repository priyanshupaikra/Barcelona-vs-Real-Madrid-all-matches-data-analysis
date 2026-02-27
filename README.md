# El Clásico Match Data Scraper and Analyzer

This project is designed to extract, clean, and analyze historical soccer match data between FC Barcelona and Real Madrid (El Clásico). The structured data is then processed for visualization, specifically through Power BI.

## Project Structure

This directory contains the following important files:

- **`dataextract.py`**: A Python web scraping script that uses `requests` and `BeautifulSoup` to scrape El Clásico match statistics from Transfermarkt. Extractions include the date, competition, home/away teams, attendance, match result, and the match winner. The extracted data is exported to `matches.csv` and `matches.xlsx`.
- **`prepare_powerbi_data.py`**: A data cleaning script using `pandas`. It takes the raw `matches.csv` file and processes it:
  - Extracts specific goal counts for FC Barcelona (`FCB_Goals`) and Real Madrid (`RMA_Goals`).
  - Calculates total goals per match.
  - Cleans attendance numbers.
  - Formats dates properly for time intelligence operations.
  - Outputs the cleaned dataset as `powerbi_matches.csv`.
- **`analysis.ipynb`**: A Jupyter Notebook used for initial exploration and analysis of the match data.
- **`elclasico.pbix`**: A Power BI dashboard file for visualizing the analyzed match statistics and trends interactively.
- **Data Files**:
  - `matches.csv` / `matches.xlsx`: The raw scraped data files.
  - `powerbi_matches.csv`: The cleaned data ready to be imported into Power BI.
 
## Data Scraping Link
# url = "https://www.transfermarkt.co.in/vergleich/vereineBegegnungen/statistik/131_418"

## Prerequisites

To run the Python scripts, you will need a few libraries. You can install them using pip:

```bash
pip install requests beautifulsoup4 pandas numpy lxml openpyxl
```

## Usage

1.  **Extract Data**:
    Run the scraper to generate the latest `matches.csv` and `matches.xlsx` files.
    ```bash
    python dataextract.py
    ```
2.  **Clean Data for Power BI**:
    Process the scraped dataset to generate the ready-to-use `powerbi_matches.csv` file.
    ```bash
    python prepare_powerbi_data.py
    ```
3.  **Visualization / Analysis**:
    - Open `elclasico.pbix` in Power BI Desktop to view the dashboard (ensure it paths to `powerbi_matches.csv`).
    - Explore patterns via `analysis.ipynb`.
