import pandas as pd
import nltk
import joblib

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# --------------------------------------------------
# Download NLTK resources
# --------------------------------------------------

nltk.download('stopwords')

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

print("=" * 60)
print("SPAM SMS DETECTION PROJECT")
print("=" * 60)

df = pd.read_csv("data/spam.csv", encoding="latin-1")

print("\nOriginal Shape:", df.shape)

# Keep only useful columns
df = df[['v1', 'v2']]

# Rename columns
df.columns = ['label', 'message']

print("New Shape:", df.shape)

# --------------------------------------------------
# Missing Values
# --------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# Remove Duplicates
# --------------------------------------------------

before = df.shape[0]

df.drop_duplicates(inplace=True)

after = df.shape[0]

print(f"\nDuplicates Removed: {before - after}")
print(f"Remaining Rows: {after}")

# --------------------------------------------------
# Convert Labels
# ham = 0
# spam = 1
# --------------------------------------------------

df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

print("\nClass Distribution:")
print(df['label'].value_counts())

# --------------------------------------------------
# Text Preprocessing
# --------------------------------------------------

ps = PorterStemmer()

stop_words = set(stopwords.words('english'))

def preprocess(text):

    text = str(text).lower()

    words = text.split()

    cleaned_words = []

    for word in words:

        if word not in stop_words:

            cleaned_words.append(
                ps.stem(word)
            )

    return " ".join(cleaned_words)

print("\nPreprocessing Text...")

df['processed_text'] = df['message'].apply(preprocess)

print("\nSample Processed Data:\n")

print(
    df[['message', 'processed_text']].head()
)

# --------------------------------------------------
# TF-IDF Vectorization
# --------------------------------------------------

print("\nCreating TF-IDF Features...")

tfidf = TfidfVectorizer(
    max_features=5000
)

X = tfidf.fit_transform(
    df['processed_text']
)

y = df['label']

print("Feature Matrix Shape:", X.shape)

# --------------------------------------------------
# Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples:", X_train.shape[0])
print("Testing Samples:", X_test.shape[0])

# --------------------------------------------------
# Train Model
# --------------------------------------------------

print("\nTraining Naive Bayes Model...")

model = MultinomialNB()

model.fit(
    X_train,
    y_train
)

print("Model Training Completed")

# --------------------------------------------------
# Predictions
# --------------------------------------------------

predictions = model.predict(X_test)

# --------------------------------------------------
# Evaluation
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions
)

recall = recall_score(
    y_test,
    predictions
)

f1 = f1_score(
    y_test,
    predictions
)

print("\n" + "=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)

# --------------------------------------------------
# Save Model
# --------------------------------------------------

joblib.dump(
    model,
    "spam_model.pkl"
)

joblib.dump(
    tfidf,
    "vectorizer.pkl"
)

print("\nModel Saved Successfully")

print("Created Files:")
print(" - spam_model.pkl")
print(" - vectorizer.pkl")

print("\nProject Completed Successfully!")