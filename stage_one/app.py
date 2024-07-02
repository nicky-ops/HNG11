from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello/<visitor_name>', methods=['GET'])
def hello(visitor_name="Mark"):
    client_ip = request.remote_addr
    ipinfo_token = '3012b04ec95bc0'
    location_response = requests.get(f'http://ipinfo.io/{client_ip}?token={ipinfo_token}')
    location_data = location_response.json()
    location = location_data.get('city', 'Huston')
    weather_api_key = '3a0d7a0f520144669f4737235ef6992f'
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={weather_api_key}")
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']

    response = {
        'client_ip': client_ip,
        'location': location,
        'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {location}',
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


