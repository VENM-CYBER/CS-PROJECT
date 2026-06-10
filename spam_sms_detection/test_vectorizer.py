import joblib

vectorizer = joblib.load("vectorizer.pkl")

print(type(vectorizer))
print("Vocabulary Size:", len(vectorizer.vocabulary_))

sample = vectorizer.transform(
    ["Congratulations! You won a free iPhone"]
)

print("Shape:", sample.shape)