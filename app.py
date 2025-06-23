from flask import Flask, render_template
from model_predict import predict_cpu_usage
import os

app = Flask(__name__)

@app.route('/')
def home():
    prediction = predict_cpu_usage()
    status = "⚠️ High usage! Consider adding a server." if prediction > 70 else "✅ Usage is normal. No action needed."
    return render_template('index.html', prediction=prediction, status=status)

if __name__ == '__main__':
    # Required for Render deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
