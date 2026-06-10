import joblib

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

while True:

    message = input("\nEnter SMS Message: ")

    if message.lower() == "exit":
        break

    vector = vectorizer.transform([message])

    prediction = model.predict(vector)

    probability = model.predict_proba(vector)

    spam_prob = probability[0][1] * 100

    if prediction[0] == 1:
        print(f"🚨 SPAM ({spam_prob:.2f}%)")
    else:
        print(f"✅ HAM ({100-spam_prob:.2f}%)")