import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os
from tqdm import tqdm
import time

load_dotenv()
APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# ✅ Updated roles list including "data engineer"
ROLES = ["data analyst", "data scientist", "ml engineer", "data engineer"]
CITIES = ["london", "manchester", "edinburgh"]

def fetch_jobs(role, location, pages=1, country="gb"):
    base_url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/"
    jobs = []

    for page in range(1, pages + 1):
        url = f"{base_url}{page}"
        params = {
            "app_id": APP_ID,
            "app_key": APP_KEY,
            "results_per_page": 50,
            "what": role,
            "where": location,
            "content-type": "application/json"
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            print(f"❌ Error {response.status_code} on {role} in {location}, page {page}")
            continue

        results = response.json().get("results", [])
        for job in results:
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company", {}).get("display_name", "N/A"),
                "location": job.get("location", {}).get("display_name", location),
                "description": job.get("description"),
                "redirect_url": job.get("redirect_url"),
                "role": role,
                "city": location,
                "scraped_at": datetime.now().strftime("%Y-%m-%d")
            })
        time.sleep(1)

    return jobs

def collect_all_jobs(pages_per_combo=2):
    all_data = []

    for role in ROLES:
        for city in CITIES:
            print(f"🔍 Scraping: {role.title()} in {city.title()}")
            jobs = fetch_jobs(role, city, pages=pages_per_combo)
            all_data.extend(jobs)

    df = pd.DataFrame(all_data)
    filename = "data/all_jobs.csv"
    df.to_csv(filename, index=False)
    print(f"\n✅ Scraped {len(df)} job records and saved to {filename}")

if __name__ == "__main__":
    collect_all_jobs(pages_per_combo=2)
