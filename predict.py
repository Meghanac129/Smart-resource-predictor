import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Read the CSV file
data = pd.read_csv('data.csv')

# Step 2: Split the data
X = data[['hour']]           # Input (hour)
y = data['cpu_usage']        # Output (CPU usage)

# Step 3: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Predict usage for next hour (hour 11)
next_hour = [[11]]
predicted = model.predict(next_hour)

# Step 5: Show prediction
print(f"Predicted CPU usage at hour 11: {predicted[0]:.2f}%")

# Step 6: Simple decision logic
if predicted[0] > 70:
    print("⚠️ High usage! Consider adding a server.")
else:
    print("✅ Usage is normal. No action needed.")

# Step 7: Plot the CPU usage
plt.plot(data['hour'], data['cpu_usage'], marker='o', color='blue', label='Actual Usage')
plt.axvline(x=11, color='red', linestyle='--', label='Next Hour')
plt.axhline(y=predicted[0], color='green', linestyle='--', label=f'Predicted: {predicted[0]:.2f}%')

plt.title("CPU Usage Over Time")
plt.xlabel("Hour")
plt.ylabel("CPU Usage (%)")
plt.legend()
plt.grid(True)
plt.show()
