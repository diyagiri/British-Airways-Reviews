import pandas as pd
import re
from collections import Counter
from textblob import TextBlob

# Load CSVs
reviews_df = pd.read_csv("ba_reviews.csv")
countries_df = pd.read_csv("Countries.csv")

# ---------------------------
# Step 1: Add Sentiment Column
# ---------------------------
def get_sentiment(text):
    blob = TextBlob(str(text))
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'

reviews_df['sentiment'] = reviews_df['content'].apply(get_sentiment)

# ---------------------------
# Step 2: Top Negative Review Keywords
# ---------------------------
custom_stopwords = set([
    'the', 'and', 'was', 'for', 'but', 'with', 'this', 'that', 'you', 'had',
    'are', 'not', 'have', 'from', 'they', 'were', 'all', 'out', 'has', 'just',
    'too', 'very', 'there', 'when', 'what', 'will', 'more', 'can', 'who', 'been',
    'one', 'about', 'their', 'get', 'your', 'only', 'did', 'would', 'which'
])

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', str(text)).lower()
    words = text.split()
    words = [word for word in words if word not in custom_stopwords and len(word) > 2]
    return words

negative_reviews = reviews_df[reviews_df['sentiment'] == 'negative']
all_words = negative_reviews['content'].apply(preprocess_text).sum()
word_freq = Counter(all_words)
top_negative_keywords = pd.DataFrame(word_freq.most_common(20), columns=['keyword', 'frequency'])

# ---------------------------
# Step 3: Sankey Flow Dataset
# ---------------------------
sankey_df = reviews_df[['traveller_type', 'seat_type', 'recommended']].dropna()
sankey_df = sankey_df.rename(columns={
    'traveller_type': 'Source',
    'seat_type': 'Target',
    'recommended': 'Outcome'
})
sankey_df = sankey_df.groupby(['Source', 'Target', 'Outcome']).size().reset_index(name='Count')

# ---------------------------
# Step 4: Clean Country/Continent Info
# ---------------------------
reviews_df['place_clean'] = reviews_df['place'].str.strip().str.title()
countries_df['Country_clean'] = countries_df['Country'].str.strip().str.title()
merged_df = pd.merge(reviews_df, countries_df, left_on='place_clean', right_on='Country_clean', how='left')
reviews_df['continent'] = merged_df['Continent']
reviews_df['region'] = merged_df['Region']

# ---------------------------
# Step 5: Save Output CSVs
# ---------------------------
reviews_df.to_csv("reviews_enriched.csv", index=False)
top_negative_keywords.to_csv("top_negative_keywords.csv", index=False)
sankey_df.to_csv("sankey_flow_data.csv", index=False)
