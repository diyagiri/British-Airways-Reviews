
# ✈️ British Airways Review Dashboard

This project explores real customer reviews of British Airways from 2016 to 2023. Using Tableau and Python, I built a dashboard that visualizes traveler sentiment, aircraft-specific performance, and key drivers of satisfaction and dissatisfaction.

---

## 📌 Project Summary

**Goal:**  
To uncover actionable insights from British Airways customer reviews by visualizing patterns in sentiment, traveler type, seat experience, and aircraft-specific feedback.

**Tools Used:**
- Python (Pandas, TextBlob, NLTK) for preprocessing and sentiment analysis
- Tableau for data visualization
- CSV files with structured review data

---

## 📊 Key Dashboard Features

| Section                                | Insight Provided                                                                 |
|----------------------------------------|----------------------------------------------------------------------------------|
| **KPI Summary Tiles**                  | Overall averages for cabin crew, food, entertainment, and value for money       |
| **Trend Line**                         | Monthly satisfaction trend for Cabin Staff Service                              |
| **Geo Map**                            | Country-wise average ratings                                                    |
| **Bar Charts**                         | Sentiment breakdown by seat type and aircraft                                   |
| **Top Complaints**                     | Most frequent negative review phrases                                           |
| **Slope Chart**                        | Recommendation rate by Traveller → Seat type                                    |
| **Quadrant Scatter Plot**             | Aircraft types by satisfaction vs review volume                                 |

---

## 💡 Business Insights

- First Class travelers have the highest positive sentiment (72%)
- Economy Class has the highest volume of negative reviews, primarily around seat comfort and delays
- Certain aircraft like Boeing 747-400 receive high volume but lower satisfaction — potential improvement area
- Solo Leisure travelers are more likely to recommend than Business travelers

---

## 🧪 Data Preparation

Python preprocessing included:
- Sentiment classification (positive/neutral/negative) using TextBlob
- Extraction of top negative keywords & bigrams
- Cleaning continent/country names for mapping
- Formatting recommendation and user journey data (e.g., Sankey-ready)

Processed datasets:
- `reviews_enriched.csv`
- `sankey_flow_data.csv`
- `top_negative_keywords.csv`

---

## 🔍 File Structure

```
📂 data/
    ├── ba_reviews.csv
    ├── Countries.csv
    ├── reviews_enriched.csv
    ├── sankey_flow_data.csv
    └── top_negative_keywords.csv

📂 python/
    └── preprocessing.py

📂 visualizations/
    └── Tableau Workbook (.twbx or .pdf screenshots)
```

---

## 🧠 What I Learned

- How to design a business-focused Tableau dashboard from raw reviews
- How to apply sentiment analysis + NLP to real user data
- How to visually segment user journeys and uncover drop-offs
- The power of combining simple metrics (satisfaction + volume) to prioritize business action

---

## 🔗 Live Dashboard / Preview

👉 [View on Tableau Public](#) *(https://public.tableau.com/views/BritishAirwaysReviews_17439106081050/ReviewDashboard?:language=en-GB&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)*  
---

