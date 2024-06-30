# Data Engineering Portfolio

## Programs Overview

This repository contains three Python programs designed for data extraction, transformation, and loading (ETL) tasks. Each program serves a specific purpose within the data engineering workflow.

### 1. Web Scraping and Data Extraction

**File:** `webscraping.py`

**Description:**
- This program performs web scraping on a list of highly-ranked films from EverybodyWiki.
- It extracts film data such as title, release year, and Rotten Tomatoes ranking.
- The extracted data is stored in both CSV (`top_50_films.csv`) and SQLite database (`Movies.db`).

**Usage:**
- Ensure Python dependencies (`requests`, `pandas`, `BeautifulSoup`) are installed.
- Install the required libraries by running `pip install -r requirements.txt` before running the script.
- Run the script to extract data from the specified URL, transform it, and load it into CSV and SQLite formats.

### 2. Data Extraction from Various Formats

**File:** `data_extraction.py`

**Description:**
- This program demonstrates data extraction from CSV, JSON, and XML files.
- It utilizes Pandas for reading data from different file types and consolidating them into a unified DataFrame.
- Extracted data is processed and logged at each phase (Extract, Transform, Load) into a log file (`log_file.txt`).

**Usage:**
- Ensure Python and required libraries (`pandas`, `xml.etree.ElementTree`) are installed.
- Install the required libraries by running `pip install -r requirements.txt` before running the script.
- Place CSV, JSON, and XML files in the same directory and run the script to execute the extraction process.

### 3. SQLite Database Operations

**File:** `sqlite_operations.py`

**Description:**
- This program demonstrates basic SQLite database operations using Pandas.
- It creates and manages tables (`INSTRUCTOR`, `Departments`) within the `STAFF.db` database.
- Includes functions for data insertion, querying, and counting records.

**Usage:**
- Ensure Python and `sqlite3` library are installed.
- Install the required libraries by running `pip install -r requirements.txt` before running the script.
- Execute the script to create tables from CSV files (`INSTRUCTOR.csv`, `Departments.csv`), insert data, and perform SQL queries.

---

### Instructions

1. **Setup:**
   - Clone this repository to your local machine.
   - Ensure Python 3.x is installed.

2. **Installing Dependencies:**
   - Navigate to the directory containing `requirements.txt`.
   - Run `pip install -r requirements.txt` to install necessary libraries.

3. **Running the Programs:**
   - Navigate to each program's directory.
   - Modify file paths or URLs as needed in the scripts.
   - Execute each script using Python (`python script_name.py`).

4. **Notes:**
   - Verify file paths, dependencies, and permissions before running the scripts.
   - Review log files (`log_file.txt`) and output files (`*.csv`, `*.db`) for results and errors.

5. **Contributions and Issues:**
   - Contributions and improvements are welcome via pull requests.
   - For issues or feedback, please raise an issue in the repository.
