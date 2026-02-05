# sitemapXML_URL_PageSpeedInsight

**Project Name**: Sitemap XML URL Extractor + PageSpeed Insight Analyzer
**Project Intro:**
This project is a Python-based automation tool that extracts all URLs from a website’s XML Sitemap Index and analyzes each page using the Google PageSpeed Insights API. It generates performance reports for both Mobile and Desktop versions of every URL, including key metrics such as Performance Score, LCP, CLS, and FID. The final results are exported into CSV files, making it easy to review and compare website performance across multiple pages efficiently 
**Features:**
- Extracts all URLs automatically from a website sitemap index XML file
- Supports multiple sitemap categories (example: post-sitemap, page-sitemap) and stores them as `url_type`
- Saves extracted URLs into a structured JSON file (`site_url.json`)
- Runs Google PageSpeed Insights API tests for each URL
- Collects important performance metrics including:
  - Performance Score
  - LCP (Largest Contentful Paint)
  - CLS (Cumulative Layout Shift)
  - FID (First Input Delay - legacy)
- Automatically classifies performance results as:
  - Good (≥ 90)
  - Moderate (50–89)
  - Bad (< 50)
- Generates two separate performance reports in CSV format:
  - `pagespeed_mobile.csv`
  - `pagespeed_desktop.csv`
- Works in bulk mode for analyzing large numbers of URLs efficiently.

**Requirements:**
- Python 3.x
- Google PageSpeed Insights API Key

Python Libraries:
- requests
- beautifulsoup4

## 🛠 Installation

### Step 1: Clone the repository in Git Bash
```bash
git clone https://github.com/fahimpyto/sitemapXML_URL_PageSpeedInsight.git
Step 2: Open the folder
cd sitemapXML_URL_PageSpeedInsight
Step 3: Install dependencies
pip install requests beautifulsoup4
Step 4: Add your Google PageSpeed Insights API key
Open main_script.py and replace:

API_KEY = "Google_Page_Speed_API"
with your actual Google PageSpeed Insights API key.
