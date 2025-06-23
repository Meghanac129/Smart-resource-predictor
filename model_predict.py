import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def predict_cpu_usage():
    data = pd.read_csv('data.csv')

    X = data[['hour']]
    y = data['cpu_usage']

    model = LinearRegression()
    model.fit(X, y)

    next_hour = [[11]]
    predicted = model.predict(next_hour)[0]

    # Save the graph
    plt.figure()
    plt.plot(data['hour'], data['cpu_usage'], marker='o', label='Actual Usage')
    plt.axvline(x=11, color='red', linestyle='--', label='Next Hour')
    plt.axhline(y=predicted, color='green', linestyle='--', label=f'Predicted: {predicted:.2f}%')
    plt.title("CPU Usage Over Time")
    plt.xlabel("Hour")
    plt.ylabel("CPU Usage (%)")
    plt.legend()
    plt.grid(True)
    plt.savefig('static/usage_plot.png')
    plt.close()

    return round(predicted, 2)
