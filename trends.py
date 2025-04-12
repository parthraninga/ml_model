
from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Define your job roles
keywords = ["QA Engineer", "Software Engineer", "Data Analyst", "DevOps Engineer", "Mobile App Developer"]

# Initialize PyTrends
pytrends = TrendReq(hl='en-US', tz=330)
pytrends.build_payload(keywords, timeframe='today 5-y')
data = pytrends.interest_over_time()

# Remove 'isPartial'
data = data.drop(columns=["isPartial"])

# Store predictions
predictions = {}

# Sequence length for LSTM input (e.g., 12 weeks)
sequence_length = 12

# Loop through each keyword
for keyword in keywords:
    df = data[[keyword]].dropna()

    # Normalize the data
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df)

    # Prepare sequences
    x, y = [], []
    for i in range(sequence_length, len(scaled_data)):
        x.append(scaled_data[i-sequence_length:i])
        y.append(scaled_data[i])

    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))

    # Build and train LSTM model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x.shape[1], 1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x, y, epochs=10, batch_size=32, verbose=0)

    # Predict the next week's trend
    last_sequence = scaled_data[-sequence_length:]
    last_sequence = np.reshape(last_sequence, (1, sequence_length, 1))
    next_week = model.predict(last_sequence)
    next_week = scaler.inverse_transform(next_week)[0][0]

    # Save prediction
    predictions[keyword] = next_week

    # Plot recent data and prediction
    plt.plot(df.index[-50:], df[keyword][-50:], label=f"{keyword} - Historical")
    plt.scatter(df.index[-1] + pd.Timedelta(weeks=1), next_week, label=f"{keyword} - Predicted", marker='x')

# Plotting
plt.title("Google Trends: Role-wise Prediction for Next Week")
plt.xlabel("Date")
plt.ylabel("Trend")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Print predictions
print("\n📈 Predicted Google Trends Interest (Next Week):")
for k, v in predictions.items():
    print(f"{k}: {v:.2f}")