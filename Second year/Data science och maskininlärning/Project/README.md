# Project – Data Science and Machine Learning

This is the final project for the course *Data Science and Machine Learning* at Dalarna University. The goal was to conduct a complete data science workflow — from data collection and preparation to clustering and statistical hypothesis testing — using real-world data.

The focus of the project was to evaluate price fairness between two major Swedish retailers: **Elgiganten** and **Komplett**, based on their laptop listings.

---

## Project Structure

### `Step 1 – Scrape Elgiganten and Komplett laptop listings/`
Python scripts and notebooks for scraping laptop data from both websites using tools such as Playwright or BeautifulSoup. Data saved in structured format (JSON/CSV).

### `Step 2 – Normalize specs and identify equivalent laptops/`
- Data cleaning and preprocessing (handling missing values, brand/model harmonization)
- Normalizing laptop specifications (RAM, CPU, GPU, SSD, screen size, etc.)
- Standardizing feature names across retailers

### `Step 3 – Group and match laptops using clustering or cosine similarity/`
- Feature engineering (e.g., TF-IDF on model names, numeric vectors from specs)
- Matching laptops using K-Means clustering and cosine similarity
- Identifying “equivalent” laptop pairs across the two retailers

### `Step 4 – Interpret results: reject or retain H₀/`
- Statistical hypothesis testing (e.g., paired t-test or Wilcoxon test)
- Null hypothesis: *There is no significant price difference between equivalent laptops sold by Elgiganten and Komplett.*
- Conclusions drawn from p-values and confidence intervals

---

## Other Contents

- `data/` – Raw and processed datasets used in the analysis  
- `Note regarding video vs. final results` – Comments on any discrepancy between presented video and final notebook output  
- `.DS_Store` – Auto-generated macOS system file (can be ignored)

---

## Tools & Libraries Used

- Python  
  - `pandas`, `numpy`, `matplotlib`, `seaborn`  
  - `scikit-learn`, `scipy`, `statsmodels`, `sklearn.metrics.pairwise`  
  - `Playwright`, `BeautifulSoup` (for scraping)

- Jupyter Notebook (analysis and reporting)

---

## Key Skills Demonstrated

- End-to-end data science workflow (collection → modeling → interpretation)
- Real-world data scraping and normalization
- Clustering and similarity matching
- Hypothesis testing and interpreting statistical significance

---

## Outcome

The analysis provided insights into pricing strategies and fairness, revealing whether either retailer tends to overprice equivalent laptop models. This type of analysis is applicable in e-commerce analytics, price monitoring tools, and consumer advocacy platforms.

---

> This project is a complete and realistic example of applied data science and hypothesis testing with real-world data.
