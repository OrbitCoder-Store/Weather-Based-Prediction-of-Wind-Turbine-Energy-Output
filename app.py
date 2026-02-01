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
    return render_template("predict.html", prediction_text="")

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
        wind_speed=speed,
        prediction_text=""
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
    prediction_rounded = round(prediction, 2)

    return render_template(
        "predict.html",
        temp=request.form.get('temp', ''),
        humid=request.form.get('humid', ''),
        pressure=request.form.get('pressure', ''),
        speed=request.form.get('speed', ''),
        wind_speed=request.form.get('wind_speed', ''),
        prediction_text=f"<div style='background: linear-gradient(135deg, #ff6b6b 0%, #ff8e72 100%); color:white; padding:20px; border-radius:8px; margin-top:25px; text-align:center; box-shadow:0 8px 20px rgba(255,107,107,0.4); border:2px solid #ff5252;'><div style='font-size:14px; font-weight:bold; letter-spacing:1px; margin-bottom:10px;'>⚡ POWER OUTPUT PREDICTION ⚡</div><div style='font-size:36px; font-weight:bold; letter-spacing:2px;'>{prediction_rounded} kW</div><div style='font-size:12px; margin-top:10px; opacity:0.95;'>Predicted Energy Output</div></div>"
    )

if __name__ == "__main__":
    app.run(debug=False)
