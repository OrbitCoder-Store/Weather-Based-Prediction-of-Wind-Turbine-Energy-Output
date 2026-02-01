import pandas as pd
import joblib
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

model = joblib.load("power_prediction.sav")

# ---------- LANDING PAGE ----------
@app.route('/')
def intro():
    return render_template("intro.html")

# ---------- PREDICT PAGE ----------
@app.route('/predict')
def predict_page():
    return render_template("predict.html")

# ---------- WEATHER ----------
@app.route('/windapi', methods=['POST'])
def windapi():
    city = request.form['city']
    api_key = "2d8ade70e9d0038838d19578f27e04db"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()

    temp = round(data['main']['temp'] - 273.15, 2)
    humid = data['main']['humidity']
    pressure = data['main']['pressure']
    speed = round(data['wind']['speed'], 2)

    return render_template(
        "predict.html",
        temp=f"{temp} °C",
        humid=f"{humid} %",
        pressure=f"{pressure} hPa",
        speed=f"{speed} m/s",
        wind_speed=speed
    )

# ---------- RESULT PAGE ----------
@app.route('/result', methods=['POST'])
def result():
    wind_speed = float(request.form['wind_speed'])
    theoretical_power = float(request.form['theoretical_power'])

    df = pd.DataFrame(
        [[wind_speed, theoretical_power]],
        columns=['WindSpeed(m/s)', 'Theoretical_Power_Curve (KWh)']
    )

    prediction = model.predict(df)[0]

    return render_template(
        "result.html",
        prediction=round(prediction, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)
