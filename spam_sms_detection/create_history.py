import pandas as pd

df = pd.DataFrame(
    columns=[
        "Time",
        "Message",
        "Prediction",
        "Spam Score"
    ]
)

df.to_csv("history.csv", index=False)

print("history.csv created successfully")