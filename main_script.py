import requests
import json
import csv
import time

API_KEY = "Google_Page_Speed_API"
JSON_FILE = "site_url.json"

def score_category(score):
    if score >= 90:
        return "Good"
    elif score >= 50:
        return "Moderate"
    else:
        return "Bad"

def run_pagespeed(url, strategy):
    api_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

    params = {
        "url": url,
        "strategy": strategy,
        "key": API_KEY,
        "category": "performance"
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    # If API returns error
    if "error" in data:
        return {
            "performance_score": "ERROR",
            "performance_status": "ERROR",
            "LCP": "ERROR",
            "CLS": "ERROR",
            "FID": "ERROR"
        }

    lighthouse = data.get("lighthouseResult")
    if not lighthouse:
        return {
            "performance_score": "N/A",
            "performance_status": "N/A",
            "LCP": "N/A",
            "CLS": "N/A",
            "FID": "N/A"
        }

    categories = lighthouse.get("categories", {})
    audits = lighthouse.get("audits", {})

    performance_data = categories.get("performance")
    if not performance_data:
        return {
            "performance_score": "N/A",
            "performance_status": "N/A",
            "LCP": "N/A",
            "CLS": "N/A",
            "FID": "N/A"
        }

    performance_score = int(performance_data.get("score", 0) * 100)

    lcp = audits.get("largest-contentful-paint", {}).get("displayValue", "N/A")
    cls = audits.get("cumulative-layout-shift", {}).get("displayValue", "N/A")

    # FID Metric (legacy)
    fid = audits.get("max-potential-fid", {}).get("displayValue", "N/A")

    return {
        "performance_score": performance_score,
        "performance_status": score_category(performance_score),
        "LCP": lcp,
        "CLS": cls,
        "FID": fid
    }

def load_urls_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    url_list = []

    for url_type, urls in data.items():
        for url in urls:
            url_list.append({
                "url_type": url_type,
                "url": url
            })

    return url_list

def save_to_csv(filename, results):
    headers = ["url_type", "url", "performance_score", "performance_status", "LCP", "CLS", "FID"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(results)

def main():
    urls = load_urls_from_json(JSON_FILE)

    mobile_results = []
    desktop_results = []

    print(f"\nTotal URLs Found: {len(urls)}\n")

    for index, item in enumerate(urls, start=1):
        url = item["url"]
        url_type = item["url_type"]

        print(f"[{index}/{len(urls)}] Testing: {url}")

        # Mobile Test
        mobile_data = run_pagespeed(url, "mobile")
        mobile_results.append({
            "url_type": url_type,
            "url": url,
            **mobile_data
        })

        # Desktop Test
        desktop_data = run_pagespeed(url, "desktop")
        desktop_results.append({
            "url_type": url_type,
            "url": url,
            **desktop_data
        })
        time.sleep(1)

    # Save CSV
    save_to_csv("pagespeed_mobile.csv", mobile_results)
    save_to_csv("pagespeed_desktop.csv", desktop_results)

    print("Work Done! CSV Files Generated:")
    print(" pagespeed_mobile.csv")
    print(" pagespeed_desktop.csv")

if __name__ == "__main__":
    main()
