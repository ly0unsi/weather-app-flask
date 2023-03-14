from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
import requests
app = Flask(__name__)


csrf = CSRFProtect(app)


@app.route("/", methods=["GET", "POST"])
@csrf.exempt
def hello():
    if (request.method == 'POST'):
        city_name = request.get_data().decode()
        r = requests.get('https://api.weatherapi.com/v1/forecast.json?key=29c12fcf303e4f3d881153742231303&q=' +
                         city_name+'&days=7&aqi=no&alerts=no&lang=fr')
        json_object = r.json()
        return jsonify(
            main_temp=json_object['current']['temp_c'],
            desc=json_object['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            city=json_object['location']['name'],
            feelLike=json_object['current']['feelslike_c'],
            wind=json_object['current']['wind_kph'],
            rainChance=json_object['forecast']['forecastday'][0]['day']['daily_chance_of_rain'],
            sunrise=json_object['forecast']['forecastday'][0]['astro']['sunrise'],
            sunset=json_object['forecast']['forecastday'][0]['astro']['sunset'],
            uv=json_object['current']['uv'],
            main_weather_icon=json_object['current']['condition']['icon'],
            forecast=json_object['forecast']['forecastday'],
            hours=json_object['forecast']['forecastday'][0]['hour'],
            lat=json_object['location']['lat'],
            long=json_object['location']['lon']
        )
    return render_template('index.html')


if __name__ == "__main__":
    app.config.setdefault('WTF_CSRF_METHODS', ['PUT'])

    app.run(debug=True)
