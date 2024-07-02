from flask import Flask, request, jsonify
import requests
import ipinfo

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = str(request.remote_addr)
    access_token = '3012b04ec95bc0'
    handler = ipinfo.getHandler(access_token)
    details = handler.getDetails()
    city = details.city
    weather_api_key = '3a0d7a0f520144669f4737235ef6992f'
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={weather_api_key}")
    weather_data = weather_response.json()
    temperature = weather_data['main']['temp']

    response = {
        'client_ip': client_ip,
        'location': city,
        'greeting': f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}',
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


