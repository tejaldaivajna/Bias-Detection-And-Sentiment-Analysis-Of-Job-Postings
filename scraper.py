import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = uc.Chrome(headless=False)

job_descriptions = []

for page in range(0, 200, 10):
    url = f"https://in.indeed.com/jobs?q=data+scientist&l=India&start={page}" # Change query and location as required
    print(f"Scraping: {url}")
    driver.get(url)
    time.sleep(8)  # wait for job cards to load

    job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")

    for index, card in enumerate(job_cards):
        try:
            # Extract metadata
            title = card.find_element(By.CSS_SELECTOR, "h2.jobTitle span").text
            company = card.find_element(By.CSS_SELECTOR, "span[data-testid='company-name']").text
            location = card.find_element(By.CSS_SELECTOR, "div[data-testid='text-location']").text

            # Click the job to open the full panel
            clickable = card.find_element(By.CSS_SELECTOR, "h2.jobTitle a")
            driver.execute_script("arguments[0].click();", clickable)
            time.sleep(3)  # wait for description panel to appear

            # Scrape full job description
            try:
                job_desc_elem = driver.find_element(By.ID, "jobDescriptionText")
                description = job_desc_elem.text.replace('\n', ' ').strip()
            except:
                description = None

            job_descriptions.append({
                "Job Title": title,
                "Company": company,
                "Location": location,
                "Description": description
            })

        except Exception as e:
            print(f"[!] Skipping job {index} on page {page}: {e}")
            continue

driver.quit()

# Save to CSV
df = pd.DataFrame(job_descriptions)
df.to_csv("job_descriptions.csv", index=False)
print("Scraped and saved successfully.")